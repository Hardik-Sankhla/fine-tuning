# fine-tuning

Repository: Fine-tuning workflows and recipes for LoRA adapters and Nemotron-style models.

## Purpose
This repo contains reproducible examples, training scripts, data preprocessing, and documentation to fine-tune open models using LoRA and related lightweight approaches.

## Structure
- `src/` — Python package and training code
- `configs/` — YAML configs for experiments and training
- `notebooks/` — interactive examples and demos
- `scripts/` — helper scripts (training, evaluation, packaging)
- `data/` — dataset storage (gitignored)
- `docs/` — documentation and guides
- `tests/` — unit and integration tests

## Quick start
1. Create a virtual env (Python 3.10+)
2. Install dependencies: `pip install -r requirements.txt`
3. Edit `configs/train.yaml` then run `scripts/train.py`

## Author
Hardik Sankhla
