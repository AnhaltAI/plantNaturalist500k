from datasets import load_dataset

dataset = load_dataset("anhaltai/inaturalist-research-grade-observations", use_auth_token=True, num_proc=16)
for instance in dataset["train"]:
    print(instance)
