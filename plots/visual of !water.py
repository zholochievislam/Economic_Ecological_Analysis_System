import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("People without water.csv")
df["positive"] = df["people_withOUT_water"] * -1

plt.figure(figsize=(12,8))
plt.barh(df["CountryName"], df["positive"])
plt.title("For 2021")
plt.ylabel("Countries")
plt.xlabel("without access")
plt.ticklabel_format(style='plain', axis='x')
plt.tight_layout()
plt.savefig("/Users/islam/PycharmProjects/PythonProject/plots/people_without_water.png", dpi=150, bbox_inches="tight")
plt.show()