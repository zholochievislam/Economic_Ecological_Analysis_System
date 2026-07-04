import pandas as pd
from pandas.errors import ParserError

from pathlib import Path

BASE_DIR = Path("/Users/islam/Desktop/univ 3rd year/Data Management/")

files = [
    "annual-co2-emissions-per-country.csv",
    "gdp-per-capita-worldbank.csv",
    "population-with-un-projections.csv",
    "inflation-of-consumer-prices.csv",
    "tree-cover-loss-by-dominant-driver.csv",
    "drinking-water-service-coverage.csv",
]

def inspect_file(filename):
    path = BASE_DIR / filename
    print("\n" + "="*80)
    print(f"File:{filename}")
    print("="*80)

    try:
        df = pd.read_csv(path)
    except ParserError:
        print("⚠ ParserError: пытаюсь прочитать с engine='python' и пропуском плохих строк...")
        df = pd.read_csv(
            path,
            engine="python",
            on_bad_lines="skip" 
        )

    print("\n Columns:")
    print(df.columns.tolist())

    print("\n First 5rows:")
    print(df.head())

    print("\n Info: ")
    print(df.info())

for f in files:
    inspect_file(f)




