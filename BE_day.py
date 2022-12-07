import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/amcaw/energizor/main/outfile.csv')

df.columns = ['Date', 'Value']

#Regex pas top, tavu

df['Date'] = df['Date'].replace({'\s\d\d:\d\d:\d\d(([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?(:([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?)+)':''}, regex = True)

df['Date'] = pd.to_datetime(df.Date, format='%Y-%m-%d')

df_grouped = df.groupby('Date')
sum_values = df_grouped.sum()

result = sum_values.apply(lambda row: row / 24, axis=1).reset_index()

result['Date'] = pd.to_datetime(result['Date'])

result.set_index('Date',inplace=True) 

new_df = result['Value'].resample('M').mean().reset_index()

new_df.to_csv('BE_day.csv')
