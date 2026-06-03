import pandas as pd

literature = pd.read_csv("../data/literature_corpus.csv")

with open("../results/summary_report.txt","w") as f:

    f.write("Visual Foundation Models Survey\n")

    f.write("\n")

    f.write("Total Papers: ")

    f.write(str(len(literature)))
