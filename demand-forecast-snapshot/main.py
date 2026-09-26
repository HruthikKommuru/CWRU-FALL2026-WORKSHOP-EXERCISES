from pathlib import Path

import pandas as pd


DATA_PATH = Path(__file__).parent / "data" / "sales_history.csv"


def main() -> None:
    sales = pd.read_csv(DATA_PATH, parse_dates=["week_start_date"])

    print(f"Shape: {sales.shape}")
    print(f"Columns: {list(sales.columns)}")
    print(
        "Date range: "
        f"{sales['week_start_date'].min().date()} to "
        f"{sales['week_start_date'].max().date()}"
    )
    print(f"Unique SKUs: {sorted(sales['sku'].unique())}")


if __name__ == "__main__":
    main()

