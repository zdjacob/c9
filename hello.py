import quandl
import pandas as pd
quandl.ApiConfig.api_key = 'RMyHsh_ctz6QyFwTMG_z'

tickers =pd.read_csv('http://www.sharadar.com/meta/sf0-tickers.txt',sep='\t')
print tickers.head()

for index, row in tickers.iterrows():
    stockCode=row['Ticker']
    priceThen = quandl.get_table('WIKI/PRICES', ticker = stockCode, date = '2016-11-01').iloc[-1]['adj_close']
    priceNow = quandl.get_table('WIKI/PRICES', ticker = stockCode, date = '2017-07-25').iloc[-1]['adj_close']
    tickers.set_value(index,'returns',(priceNow-priceThen)/priceThen)





tickers.to_csv('returns.csv')
print '\n\n\nCompleted.\n\n\n'