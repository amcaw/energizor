import pandas as pd
df2 = pd.read_csv("https://guillaumederval.github.io/endexHistory/data.csv").set_index("date")


#TTF 101
df2 = df2.loc["2022-12":]
df2 = df2.reset_index()
df2 = df2[(df2["product"] == "FEB-23") & (df2["market"] == "TFM")].value.mean()

df2 = df2[['date', 'value']]

df.to_csv("gaz_mean.csv")
