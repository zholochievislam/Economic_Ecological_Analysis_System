import pandas as pd


MERGED = "final_merged_dataset_clean_no_na.csv"

df = pd.read_csv(MERGED)


# 1. COUNTRIES
countries = df[["Entity", "Code"]].drop_duplicates().reset_index(drop=True)

# CountryID: 1, 2, 3
countries["CountryID"] = countries.index + 1

countries = countries[["CountryID", "Entity", "Code"]]
countries.to_csv("Countries.csv", index=False)

#helper: map country name -> ID
country_map = dict(zip(countries["Entity"], countries["CountryID"]))



# 2. ECONOMIC INDICATORS

econ_indicators = pd.DataFrame({
    "EconIndicatorID": [1, 2, 3],
    "IndicatorName": ["gdp_per_capita", "inflation_rate", "population"]
})
econ_indicators.to_csv("Economic_Indicators.csv", index=False)



# 3. ECOLOGIC INDICATORS
ecol_indicators = pd.DataFrame({
    "EcolIndicatorID": [1, 2, 3],
    "IndicatorName": ["co2_emissions", "safe_water_access", "forest_loss_fire"]
})
ecol_indicators.to_csv("Ecologic_Indicators.csv", index=False)

# 4. ECONOMIC DATA
econ_data = pd.DataFrame()

# GDP
tmp = df[["Entity", "Year", "gdp_per_capita"]].copy()
tmp["CountryID"] = tmp["Entity"].map(country_map)
tmp["EconIndicatorID"] = 1
tmp["Value"] = tmp["gdp_per_capita"]
econ_data = pd.concat([econ_data, tmp[["CountryID", "EconIndicatorID", "Year", "Value"]]])

# Inflation
tmp = df[["Entity", "Year", "inflation_rate"]].copy()
tmp["CountryID"] = tmp["Entity"].map(country_map)
tmp["EconIndicatorID"] = 2
tmp["Value"] = tmp["inflation_rate"]
econ_data = pd.concat([econ_data, tmp[["CountryID", "EconIndicatorID", "Year", "Value"]]])

# Population
tmp = df[["Entity", "Year", "population"]].copy()
tmp["CountryID"] = tmp["Entity"].map(country_map)
tmp["EconIndicatorID"] = 3
tmp["Value"] = tmp["population"]
econ_data = pd.concat([econ_data, tmp[["CountryID", "EconIndicatorID", "Year", "Value"]]])

econ_data = econ_data.reset_index(drop=True)

# EconDataID: '01', '02', '03'
econ_data["EcolDataID"] = "N" + (econ_data.index + 1).astype(str)

econ_data = econ_data[["EconDataID", "CountryID", "EconIndicatorID", "Year", "Value"]]
econ_data.to_csv("Economic_Data.csv", index=False)


# 5. ECOLOGIC DATA
ecol_data = pd.DataFrame()

# CO2
tmp = df[["Entity", "Year", "co2_emissions"]].copy()
tmp["CountryID"] = tmp["Entity"].map(country_map)
tmp["EcolIndicatorID"] = 1
tmp["Value"] = tmp["co2_emissions"]
ecol_data = pd.concat([ecol_data, tmp[["CountryID", "EcolIndicatorID", "Year", "Value"]]])

# Safe water
tmp = df[["Entity", "Year", "safe_water_access"]].copy()
tmp["CountryID"] = tmp["Entity"].map(country_map)
tmp["EcolIndicatorID"] = 2
tmp["Value"] = tmp["safe_water_access"]
ecol_data = pd.concat([ecol_data, tmp[["CountryID", "EcolIndicatorID", "Year", "Value"]]])

# Forest loss (fire)
tmp = df[["Entity", "Year", "forest_loss_fire"]].copy()
tmp["CountryID"] = tmp["Entity"].map(country_map)
tmp["EcolIndicatorID"] = 3
tmp["Value"] = tmp["forest_loss_fire"]
ecol_data = pd.concat([ecol_data, tmp[["CountryID", "EcolIndicatorID", "Year", "Value"]]])

ecol_data = ecol_data.reset_index(drop=True)

# EcolDataID: '001', '002', '003'
ecol_data["EcolDataID"] = "L" + (ecol_data.index + 1).astype(str)

ecol_data = ecol_data[["EcolDataID", "CountryID", "EcolIndicatorID", "Year", "Value"]]
ecol_data.to_csv("Ecologic_Data.csv", index=False)

print("Countries.csv")
print("Economic_Indicators.csv")
print("Ecologic_Indicators.csv")
print("Economic_Data.csv")
print("Ecologic_Data.csv")
