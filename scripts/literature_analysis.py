import pandas as pd

df = pd.read_csv("../data/literature_corpus.csv")

print(df["Year"].value_counts().sort_index())

print("\nTop Publication Years")
print(df.groupby("Year").size())
