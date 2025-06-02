from datasets import load_dataset

dataset = load_dataset("anhaltai/plantnet-300k", use_auth_token=True)
for split_name in dataset.keys():
    dataframe = dataset[split_name].to_pandas()
    tax_col_names_order = [
        "label",
    ]
    dataframe = dataframe.drop(columns=["image"])

    for tax_col_name in tax_col_names_order:
        dataframe[tax_col_name] = dataframe[tax_col_name].map(
            {i: name for i, name in enumerate(dataset[split_name].features[tax_col_name].names)})

    df_groups = dataframe.groupby(tax_col_names_order).size()
    df_groups.to_csv(f"plantnet-300k.{split_name}.csv", encoding="utf-8")
