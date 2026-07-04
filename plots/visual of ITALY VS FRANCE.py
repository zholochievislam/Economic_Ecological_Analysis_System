import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ITALY_VS_FRANCE.csv")

plt.figure(figsize = (12,8))
plt.plot(df["Year"], df["Italy_GDP"], marker = "o", label = "ITALY GDP")
plt.plot(df["Year"], df["France_GDP"], marker = "o", label = "France GDP")

plt.xlabel("Year")
plt.ylabel("GDP per Capita($)")
plt.title("GDP Comparison between Italy and France")
plt.grid(True, linestyle = "-.", alpha = 0.5)
#plt.legend()
plt.show()

