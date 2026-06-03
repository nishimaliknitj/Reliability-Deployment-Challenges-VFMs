import pandas as pd

literature = pd.read_csv("../data/literature_corpus.csv")
benchmark = pd.read_csv("../data/benchmark_master.csv")
weakness = pd.read_csv("../data/weakness_annotations.csv")

print("="*60)
print("SURVEY STATISTICS")
print("="*60)

print("Total Papers:", len(literature))
print("Total Benchmarks:", len(benchmark))
print("Total Weaknesses:", len(weakness))
