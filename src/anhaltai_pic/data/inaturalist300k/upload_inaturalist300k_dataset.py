from datasets import load_dataset, Dataset, NamedSplit, Split

from anhaltai_pic.data.gbif_huggingface_dataset_creator import GBIFHuggingFaceDatasetCreator

if __name__ == '__main__':
    dataset_creator = GBIFHuggingFaceDatasetCreator(
        "/storage/datasets/gbif/inaturalist-300k/data",
        "anhaltai/inaturalist-300k",
        splits=[Split.TRAIN, Split.VALIDATION, Split.TEST],
        split_dataset={Split.TRAIN: 0.8, Split.VALIDATION: 0.1, Split.TEST: 0.1},
        version="0.0.1",
    )
    dataset_creator.create("/storage/datasets/gbif/inaturalist-300k/hf_dataset")
