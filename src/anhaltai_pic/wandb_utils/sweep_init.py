import wandb
import yaml
from yaml import SafeLoader

with open('configs/sweep-config.yaml', encoding='utf-8') as config_file:
    sweep_config = yaml.load(config_file, Loader=SafeLoader)

wandb.login()

sweep_id = wandb.sweep(sweep=sweep_config)
print(sweep_id)
