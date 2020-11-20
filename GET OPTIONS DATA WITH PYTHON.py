
#https://blog.quantinsti.com/stock-market-data-analysis-python/
#https://quantra.quantinsti.com/startCourseDetails?cid=66&section_no=5&unit_no=7#course_type=paid&unit_type=Notebook
#https://pythonprogramming.net/quantopian-pyfolio-analysis-python-programming-for-finance/
from nsepy import get_history
from datetime import date
import pandas as pd
import requests
from io import BytesIO
import certifi
from scipy import stats
from dateutil.relativedelta import relativedelta
#import numpy as np
#import matplotlib.pyplot as plt

nf_opt = get_history(symbol="NIFTY",
                        start=date(2020,6,1),
                        end=date(2020,7,30),
                        index=True,
                        option_type="CE",
                        strike_price=9100,
                        expiry_date=date(2020,7,30))
'''Index(['Symbol', 'Expiry', 'Option Type', 'Strike Price', 'Open', 'High',       'Low', 'Close', 'Last', 'Settle Price', 'Number of Contracts',
       'Turnover', 'Premium Turnover', 'Open Interest', 'Change in OI',
       'Underlying'],
      dtype='object')'''
'''nf_opt.set_option('display.max_columns', None)  # or 1000
nf_opt.set_option('display.max_rows', None)  # or 1000
nf_opt.set_option('display.max_colwidth', -1)  # or 199'''
#nf_opt.set_option('display.max_columns', None)
#nf_opt.max_columns=1000
#print(nf_opt.column)
print(nf_opt)
print(nf_opt.head())


import yfinance as yf
data = yf.download('AAPL', start="2017-01-01", end="2017-04-30")
data.head()
print(data.head())
'''
import quandl
from datetime import datetime

# quantrautil is a module specific to Quantra to fetch stock data
from quantrautil import get_quantinsti_api_key
api_key = get_quantinsti_api_key()

data = quandl.get('EOD/AAPL', start_date='2017-1-1', end_date='2018-1-1', api_key= api_key)

# Note that you need to know the "Quandl code" of each dataset you download. In the above example, it is 'EOD/AAPL'.
# To get your personal API key, sign up for a free Quandl account. Then, you can find your API key on Quandl account settings page.
print("________________________")
print(data.head())'''

import pandas as pd
from pandas_datareader import data
data = data.get_data_yahoo('AAPL', '2017-01-01', '2018-01-01')
data.head()
print(data.head())

# Yahoo recently has become an unstable data source.
# If it gives an error, you may run the cell again, or try yfinance
import pandas as pd
from pandas_datareader import data
# Set the start and end date
start_date = '1990-01-01'
end_date = date.today()#'2019-02-01'
# Set the ticker
ticker = 'AMZN'
# Get the data
data = data.get_data_yahoo(ticker, start_date, end_date)
data.head()

import matplotlib.pyplot as plt
#matplotlib inline
data['Adj Close'].plot()
plt.show()

# Plot the adjusted close price
data['Adj Close'].plot(figsize=(10, 7))
# Define the label for the title of the figure
plt.title("Adjusted Close Price of %s" % ticker, fontsize=16)
# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)
# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
# Show the plot
plt.show()

import quandl
# To get your API key, sign up for a free Quandl account.
# Then, you can find your API key on Quandl account settings page.
QUANDL_API_KEY = 'AwSxXCHEuNcMv_fUohpT'
# This is to prompt you to change the Quandl Key
if QUANDL_API_KEY == 'REPLACE-THIS-TEXT-WITH-A-REAL-API-KEY':
 raise Exception("Please provide a valid Quandl API key!")
# Set the start and end date
start_date = '1990-01-01'
end_date = '2018-03-01'
# Set the ticker name
ticker = 'AMZN'
# Feth the data
data = quandl.get('WIKI/'+ticker, start_date=start_date,
 end_date=end_date, api_key=QUANDL_API_KEY)
# Print the first 5 rows of the dataframe
data.head()
print("test---------------")
print(data.head())

# Define the figure size for the plot
plt.figure(figsize=(10, 7))
# Plot the adjusted close price
data['Adj. Close'].plot()
# Define the label for the title of the figure
plt.title("Adjusted Close Price of %s" % ticker, fontsize=16)
# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)
# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.show()

# Define the ticker list
import pandas as pd
tickers_list = ['AAPL', 'IBM', 'MSFT', 'WMT']
# Import pandas
data = pd.DataFrame(columns=tickers_list)
# Feth the data
for ticker in tickers_list:
 data[ticker] = quandl.get('WIKI/' + ticker, start_date=start_date,
 end_date=end_date, api_key=QUANDL_API_KEY)['Adj. Close']
# Print first 5 rows of the data
data.head()

# Plot all the close prices
data.plot(figsize=(10, 7))
# Show the legend
plt.legend()
# Define the label for the title of the figure
plt.title("Adjusted Close Price", fontsize=16)
# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)
# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.show()


# Import TimeSeries class
from alpha_vantage.timeseries import TimeSeries
ALPHA_VANTAGE_API_KEY = 'REF5GTSBYWRUSV9KP'
# This is to prompt you to change the ALPHA_VANTAGE Key
if ALPHA_VANTAGE_API_KEY == 'REPLACE-THIS-TEXT-WITH-A-REAL-API-KEY':
 raise Exception("Please provide a valid Alpha Vantage API key!")
# Initialize the TimeSeries class with key and output format
ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')
# Get pandas dataframe with the intraday data and information of the data
intraday_data, data_info = ts.get_intraday(
 'GOOGL', outputsize='full', interval='1min')
# Print the information of the data
print(data_info)
# Print the intraday data
intraday_data.head()
intraday_data['4. close'].plot(figsize=(10, 7))
# Define the label for the title of the figure
plt.title("Close Price", fontsize=16)
# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Time', fontsize=14)
# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.show()
intraday_data.index = pd.to_datetime(intraday_data.index)
ohlcv_dict = {
 '1. open': 'first',
 '2. high': 'max',
 '3. low': 'min',
 '4. close': 'last',
 '5. volume': 'sum'
}
intraday_data_10 = intraday_data.resample('10T').agg(ohlcv_dict)
intraday_data_10.head()

# Install the yfinance if not already installed
#!pip install yfinance

# Import yfinance
import yfinance as yf
# Set the ticker as MSFT
msft = yf.Ticker("MSFT")

 #get price to book
pb = msft.info['priceToBook']
#pe = msft.info['regularMarketPrice']/msft.info['epsTrailingTwelveMonths']
print('Price to Book Ratio is: %.2f' % pb)
#print('Price to Earnings Ratio is: %.2f' % pe)
'''
# show revenues
revenue = msft.financials.loc['Total Revenue']
plt.bar(revenue.index, revenue.values)
plt.ylabel("Total Revenues")
plt.show()

EBIT = msft.financials.loc['Earnings Before Interest and Taxes']
plt.bar(EBIT.index, EBIT.values)
plt.ylabel("EBIT")
plt.show()

# show income statement
msft.financials
# show balance heet
msft.balance_sheet
# show cashflow
msft.cashflow
# show other info
msft.info
'''

from datetime import date
from nsepy import get_history
# Stock options (for index options, set index = True)
stock_fut = get_history(symbol="HDFC",
 start=date(2019, 1, 15),
 end=date(2019, 2, 1),
 futures=True,
 expiry_date=date(2019, 2, 28))
stock_fut.head()


import matplotlib.pyplot as plt
stock_fut.Close.plot(figsize=(10, 5))
# Define the label for the title of the figure
plt.title("Close Price", fontsize=16)
# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Date', fontsize=14)
# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.show()

from datetime import date
from nsepy import get_history
stock_opt = get_history(symbol="HDFC",
 start=date(2019, 1, 15),
 end=date(2019, 2, 1),
 option_type="CE",
 strike_price=2000,
 expiry_date=date(2019, 2, 28))
stock_opt.head()


import matplotlib.pyplot as plt
stock_opt.Close.plot(figsize=(10, 5))
# Define the label for the title of the figure
plt.title("Close Price", fontsize=16)
# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Date', fontsize=14)
# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.show()


# Install pyfolio if not already installed
#pip install pyfolio

import pyfolio as pf


# Define the ticker list
tickers_list = ['AAPL', 'AMZN', 'MSFT', 'WMT']
# Import pandas and create a placeholder for the data
import pandas as pd
data = pd.DataFrame(columns=tickers_list)
# Feth the data
import yfinance as yf
for ticker in tickers_list:
 data[ticker] = yf.download(ticker, period='5y',)['Adj Close']
# Compute the returns of individula stocks and then compute the daily mean returns.
# The mean return is the daily portfolio returns with the above four stocks.
data = data.pct_change().dropna().mean(axis=1)
# Print first 5 rows of the data
data.head()


pf.create_full_tear_sheet(data)



