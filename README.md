# Plant Image Classification
![banner.png](images/banner.png)

## Contents of this repo
- `configs` and `scripts` and `src` contain 
    - files related to running the code and reproducing the experiments
    - scripts used to download the GBIF dataset, and to build plantNet-500k 
- `documentation` has artifacts generated througout the process
- `paper/notebooks` contain the notebooks used to analyze the datasets and generate the plots  

## Preliminary "getting started" (TODO)
### WanDB setup
```bash
export WANDB_API_KEY=[REDACTED]
export WANDB_ENTITY=anhaltai
export WANDB_PROJECT=plant-image-classification
```
### Start sweeps
`./scripts/create_sweep.sh`


