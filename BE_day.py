import pandas as pd
import datetime as dt 

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

new_df['Value'] = new_df['Value'].round(2)

new_df['pct_change'] = new_df['Value'].pct_change()

new_df['pct_change'] = (new_df['pct_change']*100).round(2)

new_df['date_jour'] = dt.datetime.today().strftime("%e/%b/%Y")

new_df['today'] = datetime.datetime.today().strftime('%d/%m/%Y à %H:%M')

new_df.style.format({'pct_change':"{0:+g}"})

new_df.to_csv('BE_day.csv')
