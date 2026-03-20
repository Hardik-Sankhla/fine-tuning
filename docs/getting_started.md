# Getting Started

1. Create and activate a Python 3.10+ virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Edit `configs/train.yaml` to your dataset and settings.
3. Run `python scripts/train.py --config configs/train.yaml` to start a dry-run.
