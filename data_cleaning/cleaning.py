import pandas as pd


# FILE PATHS
GDP_FILE = "gdp-per-capita-worldbank.csv"
CO2_FILE = "annual-co2-emissions-per-country.csv"
WATER_FILE = "drinking-water-service-coverage.csv"
INFLATION_FILE = "inflation-of-consumer-prices.csv"
POPULATION_FILE = "population-with-un-projections.csv"
FIRE_FILE = "tree-cover-loss-by-dominant-driver.csv"

OUTPUT_FILE = "final_merged_dataset.csv"

YEAR_START = 2014
YEAR_END = 2024


def clean_basic(df, value_column):
    df = df[["Entity", "Code", "Year", value_column]]
    df = df[(df["Year"] >= YEAR_START) & (df["Year"] <= YEAR_END)]
    df = df.dropna(subset=[value_column])
    df = df.drop_duplicates(subset=["Entity", "Year"])
    df = df.sort_values(["Entity", "Year"])
    return df



# 1. GDP per capita
gdp = pd.read_csv(GDP_FILE, on_bad_lines="skip")

#['Entity', 'Code', 'Year', 'ny_gdp_pcap_pp_kd', 'owid_region']
gdp = clean_basic(gdp, "ny_gdp_pcap_pp_kd")
gdp = gdp.rename(columns={"ny_gdp_pcap_pp_kd": "gdp_per_capita"})


# 2. CO2 Emissions (emissions_total)
co2 = pd.read_csv(CO2_FILE, on_bad_lines="skip")

#['Entity', 'Code', 'Year', 'emissions_total']
co2 = clean_basic(co2, "emissions_total")
co2 = co2.rename(columns={"emissions_total": "co2_emissions"})


# 3. Drinking Water Access
water = pd.read_csv(WATER_FILE, on_bad_lines="skip")

# ['Entity','Code','Year','wat_ns_pop__residence_total','wat_unimp_pop__residence_total','wat_lim_pop__residence_total',
#'wat_baso_pop__residence_total','wat_sm_pop__residence_total']
# needed -> safely managed = wat_sm_pop__residence_total
water = clean_basic(water, "wat_sm_pop__residence_total")
water = water.rename(columns={"wat_sm_pop__residence_total": "safe_water_access"})


# 4. Inflation (Consumer prices)
inflation = pd.read_csv(INFLATION_FILE, on_bad_lines="skip")

#['Entity', 'Code', 'Year', 'fp_cpi_totl_zg']
inflation = clean_basic(inflation, "fp_cpi_totl_zg")
inflation = inflation.rename(columns={"fp_cpi_totl_zg": "inflation_rate"})


# 5. Population
pop = pd.read_csv(POPULATION_FILE, on_bad_lines="skip")

#['Entity','Code','Year','population__sex_all__age_all__variant_estimates', 'population__sex_all__age_all__variant_medium']
#needed -> variant_estimates
pop = clean_basic(pop, "population__sex_all__age_all__variant_estimates")
pop = pop.rename(columns={"population__sex_all__age_all__variant_estimates": "population"})


# 6. Tree-cover loss from wildfire
fire = pd.read_csv(FIRE_FILE, on_bad_lines="skip")

#['Entity','Code','Year', ... , 'tree_cover_loss_ha__category_wildfire']
fire = clean_basic(fire, "tree_cover_loss_ha__category_wildfire")
fire = fire.rename(columns={"tree_cover_loss_ha__category_wildfire": "forest_loss_fire"})


# MERGING EVERYTHING:
merged = gdp.merge(co2, on=["Entity", "Code", "Year"], how="outer")
merged = merged.merge(water, on=["Entity", "Code", "Year"], how="outer")
merged = merged.merge(inflation, on=["Entity", "Code", "Year"], how="outer")
merged = merged.merge(pop, on=["Entity", "Code", "Year"], how="outer")
merged = merged.merge(fire, on=["Entity", "Code", "Year"], how="outer")

merged = merged.sort_values(["Entity", "Year"])

merged.to_csv(OUTPUT_FILE, index=False)

print("Final file:", OUTPUT_FILE)
print("Countries:", merged['Entity'].nunique())
print("Rows:", len(merged))