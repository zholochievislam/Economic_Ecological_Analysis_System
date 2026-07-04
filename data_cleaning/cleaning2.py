import pandas as pd

# FILE PATHS
GDP_FILE = "gdp-per-capita-worldbank.csv"
CO2_FILE = "annual-co2-emissions-per-country.csv"
WATER_FILE = "drinking-water-service-coverage.csv"
INFLATION_FILE = "inflation-of-consumer-prices.csv"
POPULATION_FILE = "population-with-un-projections.csv"
FIRE_FILE = "tree-cover-loss-by-dominant-driver.csv"

OUTPUT_FILE = "merged_clean.csv"

YEAR_START = 2014
YEAR_END = 2024

def clean_dataset(df, value_column):
    df = df[["Entity", "Code", "Year", value_column]].copy()

    df = df[df["Year"].between(YEAR_START, YEAR_END)]
    df = df.drop_duplicates()

    return df
def read_csv_safe(path):
    try:
        return pd.read_csv(path, on_bad_lines="skip")
    except:
        return pd.read_csv(path, delimiter=";", on_bad_lines="skip")

# Load datasets
gdp = read_csv_safe(GDP_FILE)
co2 = read_csv_safe(CO2_FILE)
water = read_csv_safe(WATER_FILE)
inflation = read_csv_safe(INFLATION_FILE)
pop = read_csv_safe(POPULATION_FILE)
fire = read_csv_safe(FIRE_FILE)

# Clean
gdp = clean_dataset(gdp, "ny_gdp_pcap_pp_kd").rename(columns={"ny_gdp_pcap_pp_kd": "gdp"})
co2 = clean_dataset(co2, "emissions_total").rename(columns={"emissions_total": "co2"})
water = clean_dataset(water, "wat_sm_pop__residence_total").rename(columns={"wat_sm_pop__residence_total": "water"})
inflation = clean_dataset(inflation, "fp_cpi_totl_zg").rename(columns={"fp_cpi_totl_zg": "inflation"})
pop = clean_dataset(pop, "population__sex_all__age_all__variant_estimates").rename(columns={"population__sex_all__age_all__variant_estimates": "population"})
fire = clean_dataset(fire, "tree_cover_loss_ha__category_wildfire").rename(columns={"tree_cover_loss_ha__category_wildfire": "fire"})


merged = gdp.merge(co2, on=["Entity", "Code", "Year"], how="outer")
merged = merged.merge(water, on=["Entity", "Code", "Year"], how="outer")
merged = merged.merge(inflation, on=["Entity", "Code", "Year"], how="outer")
merged = merged.merge(pop, on=["Entity", "Code", "Year"], how="outer")
merged = merged.merge(fire, on=["Entity", "Code", "Year"], how="outer")


merged["na_count"] = merged.isna().sum(axis=1)
merged = merged[merged["na_count"] <= 2].copy()
merged = merged.drop(columns=["na_count"])


merged = merged.fillna(merged.mean(numeric_only=True))


merged.to_csv(OUTPUT_FILE, index=False)

print("Cleaning completed. Saved:", OUTPUT_FILE)
