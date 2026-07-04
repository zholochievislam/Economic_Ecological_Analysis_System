import pandas as pd
from pathlib import Path

def inspect_csv(file_path):
    print("-"*50)
    print(f"File: {file_path}")
    print("-"*50)

    # Upload first 5 lines
    try:
        df = pd.read_csv(file_path, on_bad_lines="skip")
    except:
        df = pd.read_csv(file_path, delimiter=";", on_bad_lines="skip")

    print("\n🔹 First 5 lines:")
    print(df.head())

    print("\n🔹 All Columns:")
    print(df.columns.tolist())

    # identify probable keywords
    country_cols = [c for c in df.columns if 'country' in c.lower() or 'entity' in c.lower()]
    year_cols = [c for c in df.columns if 'year' in c.lower()]
    value_cols = [c for c in df.columns if c.lower() not in (country_cols + year_cols) and df[c].dtype != 'object']

    print("\nFound country columns:", country_cols)
    print("Found country years:", year_cols)
    print("Found country values:", value_cols)

    # Type of INDICATOR
    indicator_type = "economic" if any(word in file_path.lower() for word in ["gdp", "income", "population"]) else \
                     "ecologic" if any(word in file_path.lower() for word in ["co2", "emission", "tree"]) else "unknown"

    print("\nPossible indicator type:", indicator_type)

    # Extra Columns
    useful = set(country_cols + year_cols + value_cols)
    extra_cols = [c for c in df.columns if c not in useful]

    print("\nExtra Columns:", extra_cols)

if __name__ == "__main__":
    files_to_inspect = [
        "gdp-per-capita-worldbank.csv", "annual-co2-emissions-per-country.csv", "drinking-water-service-coverage.csv",
        "inflation-of-consumer-prices.csv", "population-with-un-projections.csv", "tree-cover-loss-by-dominant-driver.csv"
    ]

    for f in files_to_inspect:
        if Path(f).exists():
            inspect_csv(f)
        else:
            print(f"File not found: {f}")