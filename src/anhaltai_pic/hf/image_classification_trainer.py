import os.path
from typing import Dict

import evaluate
import numpy as np
import torch
from sklearn.metrics import accuracy_score, label_ranking_average_precision_score
import datasets
import wandb
from PIL import Image, ImageFile
from torch.utils.data import Dataset
from datasets import ClassLabel, load_dataset, Features, DatasetDict
from transformers import AutoModelForImageClassification, AutoConfig, TrainingArguments, IntervalStrategy, Trainer, \
    EarlyStoppingCallback, AutoImageProcessor

Image.MAX_IMAGE_PIXELS = None
ImageFile.LOAD_TRUNCATED_IMAGES = True


class ImageClassificationDataset(Dataset):
    def __init__(
            self,
            dataset,
            class_name,
            transform
    ):
        super().__init__()

        self.dataset = dataset
        self.class_name = class_name
        self.transform = transform

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):
        item = self.dataset[index]
        return {"label": item[self.class_name],
                "pixel_values": self.transform(item["image"])["pixel_values"][0]}


def init_dataset(
        dataset_name: str,
        item_limit: int = 0,
) -> DatasetDict:
    dataset = load_dataset(dataset_name, token=True, num_proc=8)
    # apply item limit
    if 0 < item_limit:
        limited_dataset = DatasetDict()
        for split_name in dataset.keys():
            if item_limit < len(dataset[split_name]):
                limited_dataset[split_name] = dataset[split_name].shuffle().select(list(range(item_limit)))
            else:
                limited_dataset[split_name] = dataset[split_name]
        dataset = limited_dataset

    for split_name in dataset.keys():
        if "label" in dataset[split_name].features:
            dataset[split_name] = dataset[split_name].remove_columns([wandb.config["class_name"]])
            dataset[split_name] = dataset[split_name].rename_column("label", wandb.config["class_name"])
    return dataset


def dataset_features(dataset: DatasetDict) -> Features:
    return dataset[datasets.Split.TRAIN].features


def init_model(model_name: str, class_label: ClassLabel, load_pretrained_weights: bool):
    if load_pretrained_weights:
        model = AutoModelForImageClassification.from_pretrained(
            model_name,
            label2id={name: i for i, name in enumerate(class_label.names)},
            id2label={i: name for i, name in enumerate(class_label.names)},
            ignore_mismatched_sizes=True,
        )
    else:
        model_config = AutoConfig.from_pretrained(model_name,
                                                  label2id={name: i for i, name in enumerate(class_label.names)},
                                                  id2label={i: name for i, name in enumerate(class_label.names)},
                                                  ignore_mismatched_sizes=True,
                                                  )
        model = AutoModelForImageClassification.from_config(model_config)

    return model


accuracy_metric = evaluate.load("accuracy")


def _compute_metrics(eval_pred):
    logits, labels = eval_pred

    # Micro-averaged accuracy
    accuracy_micro = accuracy_score(labels, np.argmax(logits, axis=-1))

    # Macro-averaged accuracy
    unique_labels = np.unique(labels)
    accuracies = []
    for label in unique_labels:
        label_mask = (labels == label)
        label_accuracy = accuracy_score(labels[label_mask], np.argmax(logits[label_mask], axis=-1))
        accuracies.append(label_accuracy)
    accuracy_macro = np.mean(accuracies)

    # Mean Reciprocal Rank (MRR)
    sorted_indices = np.argsort(-logits, axis=1)
    ranks = np.zeros(labels.shape[0])
    for i, label in enumerate(labels):
        rank = np.where(sorted_indices[i] == label)[0][0] + 1
        ranks[i] = 1 / rank
    mrr = np.mean(ranks)

    return {
        "accuracy_micro": accuracy_micro,
        "accuracy_macro": accuracy_macro,
        "mean_reciprocal_rank": mrr,
    }


def train(default_config: Dict = None):
    wandb_mode = "online"
    if default_config and "wandb_mode" in default_config:
        wandb_mode = default_config["wandb_mode"]

    wandb.init(
        config=default_config,
        mode=wandb_mode,
    )

    print(f"config: {wandb.config}")

    dataset = init_dataset(
        dataset_name=wandb.config["dataset_name"],
        item_limit=wandb.config["item_limit"],
    )

    model = init_model(
        wandb.config["model_name"],
        dataset_features(dataset)[wandb.config["class_name"]],
        wandb.config["load_pretrained_weights"]
    )

    if wandb.run.sweep_id is None:
        model_path = os.path.join("models", "runs", wandb.run.id, wandb.config["model_name"])
    else:
        model_path = os.path.join("models", "sweeps", wandb.run.sweep_id, wandb.config["model_name"])

    training_args = TrainingArguments(
        output_dir=model_path,
        learning_rate=wandb.config["learning_rate"],
        per_device_train_batch_size=wandb.config["batch_size"],
        per_device_eval_batch_size=wandb.config["batch_size"],
        num_train_epochs=wandb.config["max_epochs"],
        weight_decay=0.01,
        metric_for_best_model="accuracy_micro",
        evaluation_strategy=IntervalStrategy.EPOCH,
        load_best_model_at_end=True,
        save_strategy=IntervalStrategy.EPOCH,
        save_total_limit=1,
        logging_strategy=IntervalStrategy.STEPS,
        logging_steps=10,
        report_to=["wandb"],
        # do not set to True, otherwise some models will fail with nan loss / gradients
        fp16=False,
    )
    transform = AutoImageProcessor.from_pretrained(wandb.config["model_name"])

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=ImageClassificationDataset(dataset[datasets.Split.TRAIN], wandb.config["class_name"], transform),
        eval_dataset=ImageClassificationDataset(dataset[datasets.Split.VALIDATION], wandb.config["class_name"],
                                                transform) if datasets.Split.VALIDATION in dataset else None,
        compute_metrics=_compute_metrics,
        callbacks=[EarlyStoppingCallback(early_stopping_patience=wandb.config["early_stopping_patience"])]
    )

    trainer.train()

    # evaluation
    if datasets.Split.TEST in dataset:
        test_dataset = ImageClassificationDataset(dataset[datasets.Split.TEST], wandb.config["class_name"], transform)
    elif datasets.Split.VALIDATION in dataset:
        test_dataset = ImageClassificationDataset(dataset[datasets.Split.VALIDATION], wandb.config["class_name"],
                                                  transform)
    else:
        test_dataset = None

    if test_dataset is not None:
        trainer.evaluate(test_dataset, metric_key_prefix="test")

    model_hf = wandb.config["model_name"][wandb.config["model_name"].index("/") + 1:]

    dataset_hf = wandb.config["dataset_name"]
    dataset_hf = dataset_hf[dataset_hf.index("/") + 1:]

    trainer.model.push_to_hub(f"anhaltai/{model_hf}-{dataset_hf}", private=True)

    wandb.finish()


if __name__ == "__main__":
    config = {
        "item_limit": 100,
        "wandb_mode": "online",
        "dataset_name": "anhaltai/plantnet300k-384",
        "model_name": "microsoft/swinv2-large-patch4-window12to24-192to384-22kto1k-ft",
        "max_epochs": 2,
        "batch_size": 2,
        "learning_rate": 0.0001,
        "early_stopping_patience": 5,
        "load_pretrained_weights": True,
        "class_name": "species"
    }
    train(config)
