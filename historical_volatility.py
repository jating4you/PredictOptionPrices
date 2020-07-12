import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# For making attractive and informative statistical graph
plt.style.use('seaborn-darkgrid')

#data = pd.read_csv('apple_stock_data.csv')
import yfinance as yf

msft = yf.Ticker("RELIANCE.NS")

data=msft.history(period="3mo")
print(data.columns.values) #['Open' 'High' 'Low' 'Close' 'Volume' 'Dividends' 'Stock Splits']
#print(data.describe())
filterdata=data[['Close']]
#print(filterdata)
filterdata['Log Returns'] = np.log(filterdata['Close']/filterdata['Close'].shift(1))

print(filterdata)
#Computing Historical Volatility
#he one month (or 20 trading days) historical volatility will be computed by using the DataFrame.rolling(window).std() function which computes the rolling standard deviation of data['Log Returns'] for a period of 20 trading days. The standard deviation is multiplied by 100 to compute the percentage value for volatility. The historical volatility will be stored in the DataFrame under the column header '20 day Historical Volatility'.
filterdata['20 day Historical Volatility'] = 100*filterdata['Log Returns'].rolling(window=20).std()
plt.plot(filterdata['20 day Historical Volatility'], color = 'b', label ='20 day Historical Volatility')
plt.legend(loc='best')
plt.show()