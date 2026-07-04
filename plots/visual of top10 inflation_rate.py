import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("")

plt.figure(figsize = (12,8))
plt.bar(df["CountryName"], df["Inflation_Rate"])
plt.xlabel("Country Name")
plt.ylabel("Inflation Rate")
plt.title("Highest Inflation Rate of 2021")
plt.show()