import pandas as pd

hits = pd.read_csv("data/example_hits.tsv", sep="\\t")
filtered = hits[hits["score"] >= 50].copy()
filtered = filtered.sort_values("score", ascending=False)
filtered.to_csv("results/filtered_hits.tsv", sep="\\t", index=False)
print(f"{len(filtered)} hits conserves")