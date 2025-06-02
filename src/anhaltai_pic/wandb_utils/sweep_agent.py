import os
import wandb

from anhaltai_pic.hf.image_classification_trainer import train

if __name__ == '__main__':
    wandb.login()
    wandb.agent(os.getenv('WANDB_SWEEP_ID', default='undefined'), function=train)
