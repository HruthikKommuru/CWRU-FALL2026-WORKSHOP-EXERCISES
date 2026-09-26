# Demand Forecast Snapshot

This repository contains a small dataset of weekly sales across five SKUs. It is the starting point for a graduate workshop where you will use an AI coding tool (Claude Code) to build a forecasting feature step by step during the session.

The repository intentionally begins with only data loading and a basic summary. The forecasting workflow is yours to develop.

## Setup

```bash
git clone https://github.com/YOUR-USERNAME/demand-forecast-snapshot.git
cd demand-forecast-snapshot
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

On Windows PowerShell, activate the virtual environment with:

```powershell
.venv\Scripts\Activate.ps1
```

Running `main.py` confirms that the dataset loads correctly and prints a brief summary.

## What you'll do in this exercise

1. Ask AI to explore the data and describe any trends or patterns it finds per SKU.
2. Ask AI what forecasting approaches would fit each pattern, and why.
3. Pick one approach and have AI implement it in `main.py`.
4. Plot actual vs. forecast and evaluate where it's wrong.

