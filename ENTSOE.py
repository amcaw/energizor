import os

import pandas as pd
from entsoe import EntsoePandasClient

# %% parameter definitions
client = EntsoePandasClient(api_key=os.environ['api_key'])

start = pd.Timestamp('20220101', tz ='UTC')
end = pd.Timestamp('20221231', tz ='UTC')
country_code = 'BE'  # 

day_ahead_prices_BE = client.query_day_ahead_prices(country_code, start=start, end=end)

df = day_ahead_prices_BE.to_frame('Value')

belpex_daily_avg = df.resample("D", origin="2001-01-01 00:00:00+01:00",label="left").mean()

belpex_monthly_avg = belpex_daily_avg['Value'].resample('M').mean()

belpex_monthly_avg.to_csv('./BE_day.csv')
