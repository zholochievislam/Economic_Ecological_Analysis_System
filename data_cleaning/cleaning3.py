import pandas as pd

df = pd.read_csv("merged_clean.csv")

# COUNTRIES
countries = df[["Entity", "Code"]].drop_duplicates().reset_index(drop=True)
countries["CountryID"] = countries.index + 1
countries.to_csv("Countries.csv", index=False)

# Create a map
country_map = dict(zip(countries["Entity"], countries["CountryID"]))

# ECONOMIC INDICATORS
econ_ind = pd.DataFrame({
    "EconIndicatorID": [1, 2, 3],
    "IndicatorName": ["gdp", "inflation", "population"]
})
econ_ind.to_csv("Economic_Indicators.csv", index=False)

# ECOLOGICAL INDICATORS
ecol_ind = pd.DataFrame({
    "EcolIndicatorID": [1, 2, 3],
    "IndicatorName": ["co2", "water", "fire"]
})
ecol_ind.to_csv("Ecologic_Indicators.csv", index=False)

# ECONOMIC DATA
econ = []

for col, indicator_id in [("gdp", 1), ("inflation", 2), ("population", 3)]:
    temp = df[["Entity", "Year", col]].copy()
    temp["CountryID"] = temp["Entity"].map(country_map)
    temp["EconIndicatorID"] = indicator_id
    temp["Value"] = temp[col]
    econ.append(temp[["CountryID", "EconIndicatorID", "Year", "Value"]])

econ_df = pd.concat(econ, ignore_index=True)
econ_df["EconDataID"] = econ_df.index + 1
econ_df.to_csv("Economic_Data.csv", index=False)

# ECOLOGIC DATA
ecol = []

for col, indicator_id in [("co2", 1), ("water", 2), ("fire", 3)]:
    temp = df[["Entity", "Year", col]].copy()
    temp["CountryID"] = temp["Entity"].map(country_map)
    temp["EcolIndicatorID"] = indicator_id
    temp["Value"] = temp[col]
    ecol.append(temp[["CountryID", "EcolIndicatorID", "Year", "Value"]])

ecol_df = pd.concat(ecol, ignore_index=True)
ecol_df["EcolDataID"] = ecol_df.index + 1
ecol_df.to_csv("Ecologic_Data.csv", index=False)

print("Generated all CSV files.")
