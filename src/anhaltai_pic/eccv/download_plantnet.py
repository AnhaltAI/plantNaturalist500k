import os

from datasets import load_dataset
import datasets
import huggingface_hub as hub
from PIL import Image, ImageFile

Image.MAX_IMAGE_PIXELS = None
ImageFile.LOAD_TRUNCATED_IMAGES = True

dataset = load_dataset("anhaltai/plantnet-300k", num_proc=1, cache_dir="/storage/.huggingface")

def resize(example):
    new_example={}
    new_example["image"] = example["image"].resize((384, 384), resample=Image.Resampling.BILINEAR, reducing_gap=None)
    new_example["species"]=example["label"]
    return new_example


dataset = dataset.map(resize, batched=False, num_proc=16)
dataset.save_to_disk("dataset_plantnet_tmp_384", max_shard_size="512MB")

dataset = datasets.load_from_disk("dataset_plantnet_tmp_384")
upload_success = False
while not upload_success:
    hub.login(token=os.getenv("HUGGINGFACE_TOKEN"), write_permission=True)
    try:
        dataset.push_to_hub("anhaltai/plantnet-300k-384", private=True, max_shard_size="512MB")
        upload_success = True
    except Exception as e:
        print(f"upload failed due to: {e}")
