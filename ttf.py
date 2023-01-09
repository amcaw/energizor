import pandas as pd
df = pd.read_csv("https://guillaumederval.github.io/endexHistory/data.csv").set_index("date")


#TTF 101
df = df.loc["2022-12":]
df = df.reset_index()
df = df[(df2["product"] == "FEB-23") & (df2["market"] == "TFM")].value.mean()

df.to_csv("gaz_mean.csv", index=True)
