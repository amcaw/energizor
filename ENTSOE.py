import os

import pandas as pd
from entsoe import EntsoePandasClient

import pandas as pd
from entsoe import EntsoePandasClient

import time
from time import sleep

# %% parameter definitions
client = EntsoePandasClient(api_key=os.environ['api_key'])

start = pd.Timestamp('20220101', tz ='UTC')
end = pd.Timestamp('20221231', tz ='UTC')
country_code = 'BE'  # 

day_ahead_prices_BE = client.query_day_ahead_prices(country_code, start=start, end=end)

day_ahead_prices_BE.to_csv('./outfile.csv')
