import pandas as pd

# FILE PATHS
GDP_FILE = "gdp-per-capita-worldbank (1).csv"
CO2_FILE = "annual-co2-emissions-per-country (1).csv"
WATER_FILE = "drinking-water-service-coverage.csv"
INFLATION_FILE = "inflation-of-consumer-prices.csv"
POPULATION_FILE = "population-with-un-projections.csv"
FIRE_FILE = "tree-cover-loss-by-dominant-driver.csv"

# OUTPUT
OUTPUT_FILE = "final_merged_dataset_clean_no_na.csv"

# YEAR FILTER
YEAR_START = 2014
YEAR_END = 2024

# CLEAN BASIC FUNCTION
def clean_basic(df, value_column):
    df = df[["Entity", "Code", "Year", value_column]]
    df = df[(df["Year"] >= YEAR_START) & (df["Year"] <= YEAR_END)]
    df = df.drop_duplicates(subset=["Entity", "Year"])
    df = df.sort_values(["Entity", "Year"])
    return df

# LOAD + CLEAN EACH DATASET

# 1. GDP
gdp = pd.read_csv(GDP_FILE, on_bad_lines="skip")
gdp = clean_basic(gdp, "ny_gdp_pcap_pp_kd")
gdp = gdp.rename(columns={"ny_gdp_pcap_pp_kd": "gdp_per_capita"})

# 2. CO2
co2 = pd.read_csv(CO2_FILE, on_bad_lines="skip")
co2 = clean_basic(co2, "emissions_total")
co2 = co2.rename(columns={"emissions_total": "co2_emissions"})

# 3. Water Access
water = pd.read_csv(WATER_FILE, on_bad_lines="skip")
water = clean_basic(water, "wat_sm_pop__residence_total")
water = water.rename(columns={"wat_sm_pop__residence_total": "safe_water_access"})

# 4. Inflation
inflation = pd.read_csv(INFLATION_FILE, on_bad_lines="skip")
inflation = clean_basic(inflation, "fp_cpi_totl_zg")
inflation = inflation.rename(columns={"fp_cpi_totl_zg": "inflation_rate"})

# 5. Population
pop = pd.read_csv(POPULATION_FILE, on_bad_lines="skip")
pop = clean_basic(pop, "population__sex_all__age_all__variant_estimates")
pop = pop.rename(columns={"population__sex_all__age_all__variant_estimates": "population"})

# 6. Forest loss (fire)
fire = pd.read_csv(FIRE_FILE, on_bad_lines="skip")
fire = clean_basic(fire, "tree_cover_loss_ha__category_wildfire")
fire = fire.rename(columns={"tree_cover_loss_ha__category_wildfire": "forest_loss_fire"})

# MERGING

merged = gdp.merge(co2, on=["Entity", "Code", "Year"], how="outer")
merged = merged.merge(water, on=["Entity", "Code", "Year"], how="outer")
merged = merged.merge(inflation, on=["Entity", "Code", "Year"], how="outer")
merged = merged.merge(pop, on=["Entity", "Code", "Year"], how="outer")
merged = merged.merge(fire, on=["Entity", "Code", "Year"], how="outer")

merged = merged.sort_values(["Entity", "Year"])


# REMOVE ROWS WITH TOO MANY NA + FILL REMAINING

indicator_cols = [
    "gdp_per_capita", "co2_emissions", "safe_water_access",
    "inflation_rate", "population", "forest_loss_fire"
]

# Count NA per row
merged["na_count"] = merged[indicator_cols].isna().sum(axis=1)

# REMOVE rows where more than 2 indicators are missing
merged = merged[merged["na_count"] <= 2].copy()

# FILL remaining NA with mean (per country)
for col in indicator_cols:
    merged[col] = merged.groupby("Entity")[col].transform(lambda x: x.fillna(x.mean()))
    merged[col] = merged[col].fillna(merged[col].mean())  # if country has all NA

merged = merged.drop(columns=["na_count"])

# SAVE FINAL DATASET
merged.to_csv(OUTPUT_FILE, index=False)

print("Ready!", OUTPUT_FILE)
print("Countries:", merged['Entity'].nunique())
print("Rows:", len(merged))