import pandas as pd

df = pd.read_csv("https://guillaumederval.github.io/endexHistory/data.csv").set_index("date")

#ENDEX 103
df2 = df.loc["2022-12":]
df2 = df2[(df2["product"] == "Q1-23") & (df2["market"] == "BPB")]

df2.to_csv('endex_histo.csv')

df2 = df2[(df2["product"] == "Q1-23") & (df2["market"] == "BPB")].value.mean()

df2.to_csv('endex_mean.csv')
