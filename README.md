# Demand Forecast Snapshot

This repository contains a small dataset. The AI tool we are going to use is Codex.

During this workshop, you will work with Codex to explore weekly sales across five SKUs and build a forecasting feature step by step. The repository intentionally starts with only the dataset and a small script that loads it.

## Business scenario

You are supporting the planning team at a mid-sized retailer that sells products in the home, office, kitchen, outdoor, and electronics categories. The dataset contains two years of weekly units sold for five representative SKUs.

The business wants to make better purchasing and inventory decisions. Ordering too little can lead to stockouts and missed sales, while ordering too much ties up cash and creates excess inventory. Your goal is to help the planning team understand how demand behaves for each SKU and begin building a useful forecast for future weeks.

## Setup

```bash
git clone https://github.com/YOUR-USERNAME/demand-forecast-snapshot.git
cd demand-forecast-snapshot
```

Open the cloned repository in Codex and ask it to set up the project, install the required dependencies, and run `main.py`. Codex can determine the appropriate setup for your operating system.

When setup is complete, `main.py` should load the dataset and print its shape, columns, date range, and SKUs.

## What you'll do in this exercise

1. Ask Codex to explore the data and describe any trends or patterns it finds for each SKU.
2. Ask Codex what forecasting approaches would fit each pattern, and why.
3. Pick one approach and have Codex implement it in `main.py`.
4. Plot actual sales against the forecast and evaluate where the forecast is wrong.
