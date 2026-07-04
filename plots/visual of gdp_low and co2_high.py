import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("GDP_low_CO2_high.csv")
df["positive"] = df["GDP_Change"] * -1

plt.figure(figsize = (12,8))
plt.scatter(df["positive"], df["CO2_Change"])
plt.xlabel("GDP_Change")
plt.ylabel("CO2_Change")
plt.show()