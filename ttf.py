import pandas as pd

df = pd.read_csv("https://guillaumederval.github.io/endexHistory/data.csv").set_index("date")

#TTF 101 histo

df3 = df[(df["product"] == "FEB-23") & (df["market"] == "TFM")]

df3.to_csv('ttf_histo.csv')

#TTF 101 mean

df2 = df.loc["2022-12":]

df4 = df2[(df2["product"] == "FEB-23") & (df2["market"] == "TFM")].value.mean().round(2)

df4 = pd.DataFrame([['ttf_101',df4]], columns=['name', 'Value'])

df4.to_csv('gaz_mean.csv')
