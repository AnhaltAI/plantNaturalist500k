from datasets import load_dataset, Dataset

from anhaltai_pic.data.gbif_huggingface_dataset_creator import GBIFHuggingFaceDatasetCreator

if __name__ == '__main__':
    dataset_creator = GBIFHuggingFaceDatasetCreator(
        "downloads/iNaturalist",
        "anhaltai/inaturalist-research-grade-observations-1536",
        max_image_size=1536,
        version="0.0.1",
    )
    dataset_creator.create("dataset")
