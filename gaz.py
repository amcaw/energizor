import requests
import pandas as pd

url = 'https://www.theice.com/marketdata/DelayedMarkets.shtml?getContractsAsJson=&productId=4331&hubId=7979'

#https://www.theice.com/marketdata/DelayedMarkets.shtml?getHistoricalChartDataAsJson=&marketId=5959835&historicalSpan=2
#https://www.theice.com/marketdata/DelayedMarkets.shtml?getHistoricalChartDataAsJson=&marketId=5477499&historicalSpan=2
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

response = requests.request("GET", url,headers=headers,data={})

myjson = response.json()

df = pd.DataFrame(myjson, columns=['marketStrip','lastPrice'])

df.to_csv("TTF_Contrats_Gaz_2023.csv", index=False)

******

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

df['Date'] = df['Date'].dt.strftime('%d/%m/%y')

df.to_csv("TTF_evo_gaz.csv", index=False)
