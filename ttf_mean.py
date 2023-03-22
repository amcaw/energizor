import pandas as pd
df2 = pd.read_csv("https://guillaumederval.github.io/endexHistory/data.csv").set_index("date")


#TTF 101
df2 = df2.loc["2023-03":]
df2 = df2.reset_index()
#df2 = df2[(df2["product"] == "JAN-23") & (df2["market"] == "TFM")].value.mean()
df2 = df2[(df2["product"] == "APR-23") & (df2["market"] == "TFM")].value.mean()
df2 = pd.DataFrame([['ttf_101',df2]], columns=['name', 'Value']).round(2)
df2.to_csv('gaz_mean.csv')
