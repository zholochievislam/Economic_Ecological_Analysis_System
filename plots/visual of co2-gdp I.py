import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Green Country.csv")
df["positive"] = df["CO2_Change"] * -1

plt.figure(figsize = (10,10))
plt.scatter(df["positive"], df["GDP_Change"])
plt.xlabel("CO2_Change")
plt.ylabel("GDP_Change")
plt.title("GDP vs CO2")
plt.grid(True)
plt.show()



