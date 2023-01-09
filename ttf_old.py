import requests
import pandas as pd

#TTF Global, correspond à ceci https://www.theice.com/products/27996665/Dutch-TTF-Natural-Gas-Futures/data?marketId=5477499&span=2

url = 'https://www.theice.com/marketdata/DelayedMarkets.shtml?getHistoricalChartDataAsJson=&marketId=5493476&historicalSpan=2'

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

response = requests.request("GET", url,headers=headers,data={})

myjson = response.json()

df = pd.json_normalize(myjson, 'bars')

df.columns = ['Date', 'Value']

df['Date']= pd.to_datetime(df['Date'])

df.to_csv("TTF_evo_gaz.csv", index=False)

#now to calculate BE data for january

df = df.loc[df["Date"].between("2022-01-01", "2023-01-31")]

df['Date'] = pd.to_datetime(df['Date'])

df.set_index('Date',inplace=True) 

df = df['Value'].resample('M').mean().round(2)

df.to_csv("gaz_mean.csv", index=True)
