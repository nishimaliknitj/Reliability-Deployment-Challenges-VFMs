import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/benchmark_master.csv")

df["Category"].value_counts().plot(kind="bar")

plt.tight_layout()

plt.savefig("../results/category_distribution.png")
