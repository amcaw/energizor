import pandas as pd

#df = pd.read_csv("https://guillaumederval.github.io/endexHistory/data.csv").set_index("date")

#TTF 101 histo

#df3 = df[(df["product"] == "MAR-23") & (df["market"] == "TFM")]

#df3.to_csv('ttf_histo.csv')

#TTF 101 mean

df2 = df2.loc["2023-02":]
df2 = df2.reset_index()
df2 = df2[(df2["product"] == "MAR-23") & (df2["market"] == "TFM")].value.mean()
df2 = pd.DataFrame([['ttf_101',df2]], columns=['name', 'Value'])

df2.to_csv('gaz_mean.csv')
