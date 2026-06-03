import pandas as pd

df = pd.read_csv("../data/weakness_annotations.csv")

print(df["Severity"].value_counts())

print(df["Model_Family"].value_counts())
