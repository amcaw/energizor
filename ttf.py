import pandas as pd

df = pd.read_csv("https://guillaumederval.github.io/endexHistory/data.csv").set_index("date")

#TTF 101
df2 = df.loc["2022-12":]

df4 = df2[(df2["product"] == "FEB-23") & (df2["market"] == "TFM")].value.mean().round(2)

df4 = pd.DataFrame([['endex',df4]], columns=['name', 'value'])

df4.to_csv('gaz_mean.csv')
