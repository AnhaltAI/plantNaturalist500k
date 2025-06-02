import concurrent.futures
import json
import math
import os
import random
import shutil
from typing import List, Optional, Set, Dict

import datasets
from PIL import Image, ImageFile
import huggingface_hub
from datasets import Dataset, Features, DatasetInfo, NamedSplit, DatasetDict, Split

from anhaltai_pic.data.gbif_downloader import GBIFDownloader

Image.MAX_IMAGE_PIXELS = None
ImageFile.LOAD_TRUNCATED_IMAGES = True


class GBIFHuggingFaceDatasetCreator:
    def __init__(self,
                 download_path: str,
                 repo_id: str,
                 splits: Optional[List[NamedSplit]] = None,
                 split_dataset: Optional[Dict[NamedSplit, float]] = None,
                 version: Optional[str] = "0.0.1",
                 features_float: Optional[Dict[str, float]] = None,
                 features_str: Optional[Dict[str, str]] = None,
                 class_label_names: Optional[Set[str]] = None,
                 max_image_size: Optional[int] = None,
                 num_threads=16,
                 ):
        self.download_path = download_path
        self.repo_id = repo_id
        self.splits = splits
        self.split_dataset = split_dataset
        self.version = version
        if features_float is None:
            self.features_float = {"decimalLatitude": None, "decimalLongitude": None}
        else:
            self.features_float = features_float
        if features_str is None:
            self.features_str = {"creator": None, "references": None}
        else:
            self.features_str = features_str
        if class_label_names is None:
            self.class_label_names = {"kingdom", "phylum", "class", "order", "family", "genus", "species"}
        else:
            self.class_label_names = class_label_names
        self.max_image_size = max_image_size
        self.num_threads = num_threads

    def _collect_class_label_values(self) -> Dict[str, List[str]]:
        if self.splits is None:
            dataset_split_paths = [self.download_path]
        else:
            dataset_split_paths = [os.path.join(self.download_path, str(split)) for split in self.splits]

        class_label_values_map = None
        for dataset_split_path in dataset_split_paths:
            split_class_label_values_map = {class_label_name: set() for class_label_name in self.class_label_names}

            for root, _, files in os.walk(dataset_split_path):
                for filename in files:
                    if filename == GBIFDownloader.METADATA_FILENAME:
                        with open(os.path.join(root, filename), 'r', encoding="utf-8") as metadata_file:
                            metadata = json.load(metadata_file)
                        for class_label_name in self.class_label_names:
                            split_class_label_values_map[class_label_name].add(metadata[class_label_name])

            if class_label_values_map is None:
                class_label_values_map = split_class_label_values_map
            else:
                for class_label_name in self.class_label_names:
                    class_label_values_map[class_label_name] &= split_class_label_values_map[class_label_name]

        return {class_label_name: list(sorted(class_label_values))
                for class_label_name, class_label_values in class_label_values_map.items()}

    def _resize_image(self, image: Image) -> Image:
        # Get the original width and height
        width, height = image.size

        # Calculate the aspect ratio
        aspect_ratio = width / height

        # Calculate the new dimensions while maintaining the aspect ratio
        if width > height:
            new_width = self.max_image_size
            new_height = int(new_width / aspect_ratio)
        else:
            new_height = self.max_image_size
            new_width = int(new_height * aspect_ratio)

        # Return the resized image
        return image.resize((new_width, new_height))

    def _load_image(self, media_path: str) -> Image:
        if self.max_image_size is None:
            return Image.open(media_path)

        resized_media_path = f"{media_path}.{self.max_image_size}.jpg"
        if os.path.exists(resized_media_path):
            return Image.open(resized_media_path)

        image = Image.open(media_path)
        if image.width <= self.max_image_size and image.height <= self.max_image_size:
            return image
        image = self._resize_image(image)
        image.save(resized_media_path)
        return image

    def _resize_dataset_image(self, media_path: str):
        image = self._load_image(media_path)
        image.close()

    def _resize_dataset_images(self, dataset_path: str):
        futures = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            for root, _, files in os.walk(dataset_path):
                for filename in files:
                    if filename == GBIFDownloader.METADATA_FILENAME:
                        with open(os.path.join(root, filename), 'r', encoding="utf-8") as metadata_file:
                            metadata = json.load(metadata_file)

                        for idx, media in enumerate(metadata["media"]):
                            media_path = os.path.join(root, f"media_{idx:04d}.jpg")
                            if os.path.exists(media_path):
                                futures.append(executor.submit(self._resize_dataset_image, media_path))

            # Getting results
            for future in concurrent.futures.as_completed(futures):
                _ = future.result()

    def _create_instance(self, metadata, media, image):
        instance = {"image": image}

        for class_label_name in self.class_label_names:
            instance[class_label_name] = metadata[class_label_name]

        for feature_float_name in self.features_float:
            if feature_float_name in metadata:
                instance[feature_float_name] = float(metadata[feature_float_name])
            elif feature_float_name in media:
                instance[feature_float_name] = float(media[feature_float_name])
            else:
                instance[feature_float_name] = self.features_float[feature_float_name]

        for feature_str_name in self.features_str:
            if feature_str_name in metadata:
                instance[feature_str_name] = str(metadata[feature_str_name])
            elif feature_str_name in media:
                instance[feature_str_name] = str(media[feature_str_name])
            else:
                instance[feature_str_name] = self.features_str[feature_str_name]

        return instance

    @staticmethod
    def _is_valid_instance(metadata, class_label_values_map: Dict[str, List[str]]) -> bool:
        for class_label_name, class_label_values in class_label_values_map.items():
            if metadata[class_label_name] not in class_label_values:
                return False
        return True

    def _init_generator(self, dataset_path: str, class_label_values_map: Dict[str, List[str]]):
        def dataset_generator():
            for root, _, files in os.walk(dataset_path):
                for filename in files:
                    if filename == GBIFDownloader.METADATA_FILENAME:
                        with open(os.path.join(root, filename), 'r', encoding="utf-8") as metadata_file:
                            metadata = json.load(metadata_file)

                        if not self._is_valid_instance(metadata, class_label_values_map):
                            continue

                        for idx, media in enumerate(metadata["media"]):
                            media_path = os.path.join(root, f"media_{idx:04d}.jpg")
                            if os.path.exists(media_path):
                                image = self._load_image(media_path)
                                yield self._create_instance(metadata, media, image)

        return dataset_generator

    def _create_dataset(self, dataset_path: str, class_label_values_map: Dict[str, List[str]]) -> Dataset:
        features = {"image": datasets.Image()}
        for class_label_name, class_label_values in class_label_values_map.items():
            features[class_label_name] = datasets.ClassLabel(names=class_label_values)
        for feature_float_name in self.features_float:
            features[feature_float_name] = datasets.Value(dtype="float")
        for feature_str_name in self.features_str:
            features[feature_str_name] = datasets.Value(dtype="string")

        return Dataset.from_generator(self._init_generator(dataset_path, class_label_values_map),
                                      features=Features(features),
                                      info=DatasetInfo(
                                          version=self.version,
                                      ),
                                      )

    def _copy_occurrence(self, occurrence_path: str, split_path: str):
        metadata_path = os.path.join(occurrence_path, GBIFDownloader.METADATA_FILENAME)
        with open(metadata_path, 'r',
                  encoding="utf-8") as metadata_file:
            try:
                metadata = json.load(metadata_file)
            except Exception as e:
                print(f"could not load metadata: {metadata_file}, because of exception: {e}")
                return

        target_occurrence_path = os.path.join(split_path,
                                              str(metadata["kingdomKey"]),
                                              str(metadata["phylumKey"]),
                                              str(metadata["classKey"]),
                                              str(metadata["orderKey"]),
                                              str(metadata["familyKey"]),
                                              str(metadata["genusKey"]),
                                              str(metadata["speciesKey"]),
                                              str(metadata["gbifID"]))
        os.makedirs(target_occurrence_path, exist_ok=True)
        shutil.copy2(os.path.join(occurrence_path, GBIFDownloader.METADATA_FILENAME),
                     os.path.join(target_occurrence_path, GBIFDownloader.METADATA_FILENAME))

        for idx, media in enumerate(metadata["media"]):
            media_path = os.path.join(occurrence_path, f"media_{idx:04d}.jpg")
            if os.path.exists(media_path):
                shutil.copy2(media_path, os.path.join(target_occurrence_path, f"media_{idx:04d}.jpg"))

    def _is_loadable(self, occurrence_path: str) -> bool:
        metadata_path = os.path.join(occurrence_path, GBIFDownloader.METADATA_FILENAME)
        with open(metadata_path, 'r',
                  encoding="utf-8") as metadata_file:
            try:
                metadata = json.load(metadata_file)
            except:
                return False
        found_loadable_image = False
        for idx, media in enumerate(metadata["media"]):
            media_path = os.path.join(occurrence_path, f"media_{idx:04d}.jpg")
            if os.path.exists(media_path) and self._load_image(media_path) is not None:
                found_loadable_image = True
                break
        return found_loadable_image

    def _generate_dataset_splits(self) -> str:
        split_download_path = os.path.join(os.path.dirname(self.download_path), "split")

        # collect species directories
        species_paths = set()
        for root, _, files in os.walk(self.download_path):
            for filename in files:
                if filename == GBIFDownloader.METADATA_FILENAME:
                    species_paths.add(os.path.dirname(root))

        for species_path in species_paths:
            # collect occurrences of current species
            occurrences_paths = []
            for root, _, files in os.walk(species_path):
                for filename in files:
                    if filename == GBIFDownloader.METADATA_FILENAME and self._is_loadable(root):
                        occurrences_paths.append(root)

            num_images = len(occurrences_paths)
            if num_images < 3:
                continue

            # Calculate the number of images for each split
            val_count = max(math.floor(self.split_dataset[Split.VALIDATION] * num_images), 1)
            test_count = max(math.floor(self.split_dataset[Split.TEST] * num_images), 1)
            train_count = num_images - val_count - test_count
            if train_count < 1:
                continue

            random.shuffle(occurrences_paths)

            # copy data into split directories
            for occurrence_path in occurrences_paths[:train_count]:
                self._copy_occurrence(occurrence_path, os.path.join(split_download_path, str(Split.TRAIN)))
            for occurrence_path in occurrences_paths[train_count:train_count + val_count]:
                self._copy_occurrence(occurrence_path, os.path.join(split_download_path, str(Split.VALIDATION)))
            for occurrence_path in occurrences_paths[train_count + val_count:]:
                self._copy_occurrence(occurrence_path, os.path.join(split_download_path, str(Split.TEST)))

        return split_download_path

    def create(self, local_dataset_path: str, max_shard_size: str = "512MB", load_local_dataset: bool = True):
        dataset = None
        if load_local_dataset and os.path.exists(local_dataset_path):
            try:
                dataset = datasets.load_from_disk(local_dataset_path)
                print(f"successfully loaded dataset from path: {local_dataset_path}")
            except Exception as e:
                print(f"could not load local dataset from path: {local_dataset_path} due to: {e}")

        if dataset is None:
            # split dataset if specified
            if self.split_dataset is not None:
                self.download_path = self._generate_dataset_splits()

            # collect feature information
            print("scan download path and collect information")
            class_label_values_map = self._collect_class_label_values()
            if self.max_image_size is not None:
                self._resize_dataset_images(self.download_path)

            # build dataset
            print("build dataset")
            if self.splits is None or len(self.splits) == 0:
                dataset = self._create_dataset(self.download_path, class_label_values_map)
            else:
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    futures = [executor.submit(self._create_dataset, os.path.join(self.download_path, str(split)),
                                               class_label_values_map)
                               for split in self.splits]
                    results = [future.result() for future in futures]
                dataset = DatasetDict({str(split): dataset for split, dataset in zip(self.splits, results)})
            dataset.save_to_disk(local_dataset_path, max_shard_size=max_shard_size)

        # upload dataset
        print("upload dataset")
        dataset = datasets.load_from_disk(local_dataset_path)
        print(f"dataset: {dataset}")

        upload_success = False
        while not upload_success:
            huggingface_hub.login(token=os.getenv("HUGGINGFACE_TOKEN"))
            try:
                dataset.push_to_hub(self.repo_id, private=True, max_shard_size=max_shard_size)
                upload_success = True
            except Exception as e:
                print(f"upload failed due to: {e}")
