from typing import Any, Optional

import pytorch_lightning as pl
import torchmetrics
import torch.nn.functional as F
from datasets import ClassLabel
from pytorch_lightning.utilities.types import STEP_OUTPUT
from transformers import AutoImageProcessor, AutoModelForImageClassification, AutoConfig
import torch
from transformers.modeling_outputs import ImageClassifierOutputWithNoAttention


class ImageClassificationModule(pl.LightningModule):
    def __init__(self, model_name: str, class_label: ClassLabel, load_pretrained_weights: bool):
        super().__init__()

        self.model_name = model_name

        if load_pretrained_weights:
            self.model = AutoModelForImageClassification.from_pretrained(
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
            self.model = AutoModelForImageClassification.from_config(model_config)

        self.accuracy = torchmetrics.Accuracy("multiclass", num_classes=len(class_label.names))

        self.save_hyperparameters()

    def configure_optimizers(self) -> Any:
        return torch.optim.Adam(self.parameters(), lr=1e-3)

    def forward(self, batch, *args: Any, **kwargs: Any) -> ImageClassifierOutputWithNoAttention:
        return self.model(batch)

    def _step(self, prefix: str, batch, *args: Any, **kwargs: Any) -> STEP_OUTPUT:
        x, y = batch["pixel_values"], batch["label"]
        output = self.forward(x)

        loss = F.cross_entropy(output.logits, y)
        predictions = torch.argmax(output.logits, dim=1)
        acc = self.accuracy(predictions, y)

        self.log(f"{prefix}/loss", loss, on_step=True, on_epoch=True, prog_bar=True, logger=True)
        self.log(f"{prefix}/accuracy", acc, on_step=True, on_epoch=True, prog_bar=True, logger=True)
        return loss

    def training_step(self, batch, *args: Any, **kwargs: Any) -> STEP_OUTPUT:
        return self._step("train", batch, args, kwargs)

    def validation_step(self, batch, *args: Any, **kwargs: Any) -> Optional[STEP_OUTPUT]:
        return self._step("val", batch, args, kwargs)

    def test_step(self, batch, *args: Any, **kwargs: Any) -> Optional[STEP_OUTPUT]:
        return self._step("test", batch, args, kwargs)
