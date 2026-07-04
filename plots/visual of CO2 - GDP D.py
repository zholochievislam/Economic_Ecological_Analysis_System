import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Clean_developing_country.csv")
df = df.sort_values("eco_efficiency_score", ascending=True)


plt.figure(figsize = (12,8))
plt.barh(df["CountryName"], df["eco_efficiency_score"])
plt.xlabel("eco_efficiency_score")
plt.ylabel("Country Name")
plt.title("GDP vs CO2 2023")
plt.grid(True)
plt.show()



