import pandas as pd

df = pd.read_csv("../data/literature_corpus.csv")

trend = df.groupby("Year").size()

for year,count in trend.items():
    print(year,count)
