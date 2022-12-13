import os

import pandas as pd
from entsoe import EntsoePandasClient

from datetime import datetime, timedelta
import datetime as dt

# %% parameter definitions
client = EntsoePandasClient(api_key=os.environ['api_key'])

start = pd.Timestamp('20220101', tz ='UTC')
end = pd.Timestamp('20221231', tz ='UTC')
country_code = 'BE'  # 

day_ahead_prices_BE = client.query_day_ahead_prices(country_code, start=start, end=end)

df = day_ahead_prices_BE.to_frame('Value')

df = df.resample("M", origin="2001-01-01 00:00:00+01:00",label="left").mean()

df['date_jour'] = dt.datetime.today().strftime("%e/%m/%Y")

df['pct_change'] = df['Value'].pct_change()

df['pct_change'] = (df['pct_change']*100).round(2)

df.to_csv('./BE_day.csv')
