import os.path
from typing import Dict

import torch
import wandb

import pytorch_lightning as pl
from pytorch_lightning.callbacks import EarlyStopping, ModelCheckpoint
from pytorch_lightning.loggers import WandbLogger
from pytorch_lightning.trainer.connectors.accelerator_connector import _AcceleratorConnector

from anhaltai_pic.image_classification_data_module import ImageClassificationDataModule
from anhaltai_pic.image_classification_module import ImageClassificationModule

torch.set_float32_matmul_precision("high")


def train(default_config: Dict = None):
    wandb_mode = "online"
    if default_config and "wandb_mode" in default_config:
        wandb_mode = default_config["wandb_mode"]

    wandb.init(
        config=default_config,
        mode=wandb_mode,
    )

    print(f"config: {wandb.config}")

    data = ImageClassificationDataModule(
        dataset_name="anhaltai/plantnet-300k",
        model_name=wandb.config["model_name"],
        batch_size=wandb.config["batch_size"],
        item_limit=wandb.config["item_limit"],
    )
    data.prepare_data()

    model = ImageClassificationModule(wandb.config["model_name"],
                                      data.features["label"],
                                      wandb.config["load_pretrained_weights"],
                                      )

    wandb_logger = WandbLogger(
        offline=wandb_mode == "offline",
        log_model=True,
    )

    if wandb_logger.experiment.sweep_id is None:
        model_path = os.path.join("models", "runs", wandb_logger.experiment.id, wandb.config["model_name"])
    else:
        model_path = os.path.join("models", "sweeps", wandb_logger.experiment.sweep_id, wandb.config["model_name"])
    checkpoint_callback = ModelCheckpoint(dirpath=model_path,
                                          filename="best",
                                          monitor="val/accuracy_epoch",
                                          mode="max",
                                          save_last=True,
                                          save_top_k=1,
                                          )
    early_stop_callback = EarlyStopping(monitor="val/accuracy_epoch",
                                        min_delta=0.0,
                                        patience=wandb.config["early_stopping_patience"], verbose=True,
                                        mode="max")

    trainer = pl.Trainer(
        logger=wandb_logger,
        max_epochs=wandb.config["max_epochs"],
        callbacks=[checkpoint_callback, early_stop_callback],
    )
    trainer.fit(model, data)

    # -hack- workaround for some CUDA re-initialization bug that I don't have the time for now
    trainer._accelerator_connector = _AcceleratorConnector(accelerator="cpu")
    trainer.test(model=model, ckpt_path=checkpoint_callback.best_model_path, datamodule=data)

    wandb.finish()


if __name__ == "__main__":
    config = {
        "item_limit": 100,
        "wandb_mode": "online",
        "model_name": "google/vit-base-patch16-224",
        "max_epochs": 3,
        "batch_size": 64,
        "lr": 0.0001,
        "early_stopping_patience": 5,
        "load_pretrained_weights": True,
    }
    train(config)
