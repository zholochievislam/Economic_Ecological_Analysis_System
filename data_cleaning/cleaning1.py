import pandas as pd

def inspect_csv(file_path):
    print("="*60)
    print("FILE:", file_path)
    print("="*60)

    # Try reading CSV
    try:
        df = pd.read_csv(file_path)
    except:
        df = pd.read_csv(file_path, delimiter=";")

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData types:")
    print(df.dtypes)

    # Basic checks
    print("\nMissing values per column:")
    print(df.isna().sum())

    print("\nNumber of rows:", len(df))
    print("Number of columns:", df.shape[1])
    print()

if __name__ == "__main__":
    files = [
        "gdp-per-capita-worldbank.csv",
        "annual-co2-emissions-per-country.csv",
        "drinking-water-service-coverage.csv",
        "inflation-of-consumer-prices.csv",
        "population-with-un-projections.csv",
        "tree-cover-loss-by-dominant-driver.csv"
    ]

    for file in files:
        try:
            inspect_csv(file)
        except FileNotFoundError:
            print("File not found:", file)
