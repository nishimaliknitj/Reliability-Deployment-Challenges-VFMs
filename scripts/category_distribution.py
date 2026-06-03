import pandas as pd

df = pd.read_csv("../data/literature_corpus.csv")

print(df["Category"].value_counts())
