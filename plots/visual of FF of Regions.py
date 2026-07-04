import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Forest_fire among the region.csv")

plt.figure(figsize = (8,8))
plt.pie(
    df["TotalFireLoss"],
    labels = df["Region"],
    autopct = "%1.1f%%",
    startangle = 90)
plt.title("Forest Fire Distribution Among Regions")
plt.tight_layout()
plt.show()
