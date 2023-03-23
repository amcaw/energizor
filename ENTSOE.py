import os

import pandas as pd
from pandas.tseries.offsets import DateOffset

from entsoe import EntsoePandasClient

from datetime import datetime, timedelta
import datetime as dt

# %% parameter definitions
client = EntsoePandasClient(api_key=os.environ['api_key'])

start = pd.Timestamp('20220101', tz ='UTC')
end = pd.Timestamp('20231231', tz ='UTC')
country_code = 'BE'  # 

day_ahead_prices_BE = client.query_day_ahead_prices(country_code, start=start, end=end)

df = day_ahead_prices_BE.to_frame('Value')

df.index.names = ['Date']

df = df.resample("M", origin="2001-01-01 00:00:00+01:00",label="left").mean()

#la ligne pour reformater la date en mois/année (c'est ma foi plus joli)

df.index = (pd.to_datetime(df.index) + DateOffset(months=1)).strftime('%m/%Y')

df['Value'] = df['Value'].round(2)

df['date_jour'] = dt.datetime.today().strftime("%e/%m/%Y")

df['pct_change'] = df['Value'].pct_change()

df['pct_change'] = (df['pct_change']*100).round(2)

df.to_csv('./BE_day.csv')
