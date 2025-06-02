from pathlib import Path
from dataclasses import dataclass
from typing import Optional

CONFIGS_DIR = Path(__file__).parent.parent.parent / "configs"
oc_cfg_file_location = CONFIGS_DIR / "omega-config.yaml"

config_exclude_keys=["HF_hub_token"]

@dataclass
class TrainingConfig:
    dataset_name: str = "anhaltai/plantnet-300k"

    # Can be "enabled", "disabled", or "offline"
    wandb_mode: str = "disabled"

    # hyperparameters
    batch_size: int = 100
    epochs: int = 100
    lr: int = 1
