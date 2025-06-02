import math
import os
import random
import threading
from typing import Dict, List

import datasets
import pandas as pd
import progressbar

df = pd.read_csv("/storage/datasets/gbif/inaturalist-300k/occurrence_focus.csv", encoding="utf-8")

# Step 1: Compute the frequency of each speciesKey
species_key_counts = df['speciesKey'].value_counts()

# Step 2: Create a Boolean mask for speciesKeys with frequency >= 4
mask = df['speciesKey'].isin(species_key_counts[species_key_counts >= 4].index)

# Step 3: Apply the mask to filter out the rows
df = df[mask]
species_key_counts = df['speciesKey'].value_counts()


def sample_species_keys(sorted_species, num_sampled_species=1000):
    num_species = len(sorted_species)

    high_freq_species = random.sample(sorted_species[:num_species // 4], num_sampled_species // 4)
    mid_freq_species = random.sample(sorted_species[num_species // 4:num_species - num_species // 4],
                                     num_sampled_species // 4)
    low_freq_species = random.sample(sorted_species[num_species - num_species // 4:], num_sampled_species // 2)

    return high_freq_species, mid_freq_species, low_freq_species


high_freq_species, mid_freq_species, low_freq_species = sample_species_keys(list(species_key_counts.index.astype(int)),
                                                                            1000)
species_keys = high_freq_species + mid_freq_species + low_freq_species

species_map = df.groupby("speciesKey")["gbifID"].apply(list).to_dict()
species_map = {key: value for key, value in species_map.items() if key in species_keys}

# Sample species distribution

# Step 1: Calculate the total number of occurrences
total_occurrences = sum(len(occurrences) for occurrences in species_map.values())

# Step 2: Determine the sampling ratio
sampling_ratio = 300000 / total_occurrences

# Step 3: Create an empty dictionary for the sampled data
species_occurrences_map = {}

# Step 4-8: Iterate over speciesKeys and sample occurrences
gbif_ids = []
for species_key, occurrences in species_map.items():
    # Step 6: Sample a subset of occurrences
    sampled_occurrences = random.sample(occurrences, max(4, math.ceil(len(occurrences) * sampling_ratio)))
    # Step 7: Store the sampled subset in the new dictionary
    species_occurrences_map[species_key] = sampled_occurrences
    gbif_ids.extend(sampled_occurrences)

print(f"total occurrences: {sum(len(occurrences) for occurrences in species_occurrences_map.values())}")

df = df[df["gbifID"].isin(gbif_ids)]
print(df.describe())
df.to_csv("/storage/datasets/gbif/inaturalist-300k/occurrence.txt", sep="\t", encoding="utf-8", index=False)
