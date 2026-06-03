import pandas as pd

df = pd.read_csv("../data/benchmark_master.csv")

missing = df[df["Value"].isna()]

print("Missing Benchmark Entries")
print(len(missing))
