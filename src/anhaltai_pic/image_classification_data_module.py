import datasets
import pytorch_lightning as pl
import torch
from PIL import Image, ImageFile
from datasets import load_dataset
from pytorch_lightning.trainer.states import TrainerFn
from torch.utils.data import DataLoader, Dataset
from pytorch_lightning.utilities.types import EVAL_DATALOADERS, TRAIN_DATALOADERS
from transformers import AutoImageProcessor

Image.MAX_IMAGE_PIXELS = None
ImageFile.LOAD_TRUNCATED_IMAGES = True


class FeatureProcessor:
    def __init__(self, feature_extractor):
        self.feature_extractor = feature_extractor

    def process(self, instance):
        return self.feature_extractor(instance["image"])


class ImageClassificationDataModule(pl.LightningDataModule):
    def __init__(self,
                 dataset_name: str,
                 model_name: str,
                 batch_size: int = 16,
                 num_proc: int = 16,
                 item_limit: int = 0,
                 ):
        super().__init__()

        self.dataset_name = dataset_name
        self.model_name = model_name
        self.batch_size = batch_size
        self.num_proc = num_proc
        self.item_limit = item_limit

        self.dataset = None
        self.features = None
        self.train_data = None
        self.val_data = None
        self.test_data = None

        self.feature_processor = None

    def prepare_data(self) -> None:
        self.dataset = load_dataset(self.dataset_name, use_auth_token=True, num_proc=self.num_proc)
        self.features = self.dataset[datasets.Split.TRAIN].features
        self.feature_processor = FeatureProcessor(AutoImageProcessor.from_pretrained(self.model_name))

    def setup(self, stage: str) -> None:
        match stage:
            case TrainerFn.FITTING:
                self.train_data = self._load_and_transform(self.dataset, datasets.Split.TRAIN)
                self.val_data = self._load_and_transform(self.dataset, datasets.Split.VALIDATION)
            case TrainerFn.VALIDATING:
                self.val_data = self._load_and_transform(self.dataset, datasets.Split.VALIDATION)
            case TrainerFn.TESTING:
                self.test_data = self._load_and_transform(self.dataset, datasets.Split.TEST)
            case _:
                raise ValueError(f"found unknown stage: {stage}")

    def _load_and_transform(self, dataset, split_name):
        # select split
        dataset = dataset[split_name]
        # apply item limit
        if 0 < self.item_limit < len(dataset):
            dataset = dataset.select(list(range(self.item_limit)))
        # preprocess
        dataset = dataset.map(self.feature_processor.process, remove_columns=["image"], num_proc=self.num_proc)
        return ImageClassificationDataset(dataset)

    def train_dataloader(self) -> TRAIN_DATALOADERS:
        return DataLoader(self.train_data, shuffle=True, batch_size=self.batch_size, num_workers=self.num_proc)

    def val_dataloader(self) -> EVAL_DATALOADERS:
        return DataLoader(self.val_data, batch_size=self.batch_size, num_workers=self.num_proc)

    def test_dataloader(self) -> EVAL_DATALOADERS:
        return DataLoader(self.test_data, batch_size=self.batch_size, num_workers=self.num_proc)


class ImageClassificationDataset(Dataset):
    def __init__(
            self,
            dataset,
    ):
        super().__init__()

        self.dataset = dataset

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):
        item = self.dataset[index]
        return {"label": item["label"],
                "pixel_values": torch.Tensor(item["pixel_values"][0])}
