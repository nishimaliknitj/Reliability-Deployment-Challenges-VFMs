import pandas as pd

df = pd.read_csv("../data/benchmark_master.csv")

print(df["Category"].value_counts())

print(df.groupby("Metric").size())
