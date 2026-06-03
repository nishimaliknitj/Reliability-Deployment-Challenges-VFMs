import pandas as pd

df = pd.read_csv("../data/literature_corpus.csv")

for _,row in df.iterrows():
    print(row["Paper_ID"], row["Reference_No"])
