import requests
import pandas as pd

#TTF Global, correspond à ceci https://www.theice.com/products/27996665/Dutch-TTF-Natural-Gas-Futures/data?marketId=5477499&span=2

url = 'https://www.theice.com/marketdata/DelayedMarkets.shtml?getHistoricalChartDataAsJson=&marketId=5477499&historicalSpan=2'

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

response = requests.request("GET", url,headers=headers,data={})

myjson = response.json()

df = pd.json_normalize(myjson, 'bars')

df.columns = ['Date', 'Value']

df['Date']= pd.to_datetime(df['Date'])

df = df.loc[df["Date"].between("2022-12-01", "2022-12-31")]

df['Date'] = pd.to_datetime(df['Date'])

df.set_index('Date',inplace=True) 

df = df['Value'].resample('Y').mean()

df.to_csv("gaz_mean.csv", index=False)
