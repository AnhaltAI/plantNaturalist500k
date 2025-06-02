import os
from typing import Dict

from transformers import Trainer, TrainingArguments
import numpy as np
from datasets import load_metric
import datasets
import torch
import torch.nn as nn
import pytorch_lightning as pl
from datasets import Dataset, ClassLabel, load_dataset
from pytorch_lightning.callbacks import EarlyStopping
from torch.utils.data import DataLoader
from torchmetrics import Accuracy
from transformers import SwinForImageClassification, AutoImageProcessor, AutoModelForImageClassification
from pytorch_lightning.loggers import WandbLogger


class MyLitModel(pl.LightningModule):
    def __init__(self, class_label: ClassLabel):
        super().__init__()
        self.model = AutoModelForImageClassification.from_pretrained(os.environ["CV_MODEL_NAME"],
                                                                     num_labels=class_label.num_classes,
                                                                     id2label={str(i): c for i, c in
                                                                               enumerate(class_label.names)},
                                                                     label2id={c: str(i) for i, c in
                                                                               enumerate(class_label.names)},
                                                                     ignore_mismatched_sizes=True, )

        self.loss_fn = nn.CrossEntropyLoss()
        self.train_accuracy = Accuracy(task="multiclass", num_classes=class_label.num_classes)
        self.val_accuracy = Accuracy(task="multiclass", num_classes=class_label.num_classes)

    def forward(self, x):
        return self.model(x)

    def training_step(self, batch, batch_idx):
        x, y = batch["pixel_values"], batch["label"]
        logits = self(x).logits

        loss = self.loss_fn(logits, y)
        self.log("train_loss", loss)

        acc = self.train_accuracy(logits, y)
        self.log("train_accuracy", acc)

        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch["pixel_values"], batch["label"]
        logits = self(x).logits

        loss = self.loss_fn(logits, y)
        self.log("val_loss", loss)

        acc = self.val_accuracy(logits, y)
        self.log("val_accuracy", acc)

    def test_step(self, batch, batch_idx):
        x, y = batch["pixel_values"], batch["label"]
        logits = self(x).logits

        loss = self.loss_fn(logits, y)
        self.log("test_loss", loss)

        acc = self.val_accuracy(logits, y)
        self.log("test_accuracy", acc)

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=0.001)


if __name__ == '__main__':
    os.environ["CV_MODEL_NAME"] = "microsoft/swin-base-patch4-window12-384-in22k"
    # os.environ["CV_MODEL_NAME"] = "microsoft/swinv2-base-patch4-window12to16-192to256-22kto1k-ft"
    # os.environ["CV_MODEL_NAME"] = "microsoft/resnet-152"
    #
    os.environ["BATCH_SIZE"] = "8"

    dataset = load_dataset("anhaltai/plantNaturalist500k-384", num_proc=1, cache_dir="/storage/.huggingface")

    # data
    feature_processor = AutoImageProcessor.from_pretrained(os.environ["CV_MODEL_NAME"])
    def _transform(example_batch):
        # Take a list of PIL images and turn them to pixel values
        inputs = feature_processor([x.convert('RGB') for x in example_batch['image']], return_tensors='pt')
        inputs["label"] = example_batch["species"]
        return inputs

    dataset = dataset.with_transform(_transform)


    def collate_fn(batch):
        # data collator
        return {
            'pixel_values': torch.stack([x['pixel_values'] for x in batch]),
            'labels': torch.tensor([x['label'] for x in batch])
        }


    metric = load_metric("accuracy")


    def compute_metrics(p):
        # function which calculates accuracy for a certain set of predictions
        return metric.compute(predictions=np.argmax(p.predictions, axis=1), references=p.label_ids)

    class_label = dataset["train"].features["species"]

    model = AutoModelForImageClassification.from_pretrained(os.environ["CV_MODEL_NAME"],
                                                            num_labels=class_label.num_classes,
                                                            id2label={str(i): c for i, c in
                                                                      enumerate(class_label.names)},
                                                            label2id={c: str(i) for i, c in
                                                                      enumerate(class_label.names)},
                                                            ignore_mismatched_sizes=True, )

    atch_size = 16
    # Defining training arguments (set push_to_hub to false if you don't want to upload it to HuggingFace's model hub)
    training_args = TrainingArguments(
        f"swin-finetuned-food101",
        remove_unused_columns=False,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        learning_rate=5e-5,
        per_device_train_batch_size=batch_size,
        gradient_accumulation_steps=4,
        per_device_eval_batch_size=batch_size,
        num_train_epochs=3,
        warmup_ratio=0.1,
        logging_steps=10,
        load_best_model_at_end=True,
        metric_for_best_model="accuracy",
        push_to_hub=True,
    )

    # Instantiate the Trainer object
    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=collate_fn,
        compute_metrics=compute_metrics,
        train_dataset=prepared_ds["train"],
        eval_dataset=prepared_ds["validation"],
        tokenizer=feature_extractor,
    )

    data = ImageDataModule(dataset, batch_size=int(os.environ["BATCH_SIZE"]))
    model = MyLitModel(dataset[datasets.Split.TRAIN].features["species"])

    wandb_logger = WandbLogger(log_model="all")

    trainer = pl.Trainer(
        max_epochs=100,
        accelerator="auto",
        devices="auto",
        callbacks=EarlyStopping('val_loss', patience=5),
        logger=wandb_logger,
    )

    trainer.fit(model, datamodule=data)
    trainer.test(ckpt_path="best", datamodule=data)
