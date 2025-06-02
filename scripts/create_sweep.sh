#!/bin/bash

# TODO create fancy deployment that first inits the sweep and afterwards passes the sweep id to the experiment containers
WANDB_SWEEP_ID=$(PYTHONPATH=src python -m anhaltai_pic.wandb_utils.sweep_init | tail -n 1)
echo "${WANDB_SWEEP_ID}"

kubectl delete configmap sweep-config --namespace=paper-plants
kubectl create configmap sweep-config --namespace=paper-plants \
  --from-literal=WANDB_API_KEY="${WANDB_API_KEY}" \
  --from-literal=WANDB_ENTITY="${WANDB_ENTITY}" \
  --from-literal=WANDB_PROJECT="${WANDB_PROJECT}" \
  --from-literal=WANDB_SWEEP_ID="${WANDB_SWEEP_ID}" \
  --from-literal=HUGGINGFACE_TOKEN="${HUGGINGFACE_TOKEN}" \
  --from-file=sweep_config.yaml=configs/sweep-config.yaml

kubectl apply -f configs/sweep-agent-pod.yaml
