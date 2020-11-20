import numpy as np
import pandas as pd
from pandas_datareader import data as web
from scipy.stats import norm
import matplotlib.pyplot as plt

import quandl
# To get your API key, sign up for a free Quandl account.
# Then, you can find your API key on Quandl account settings page.
QUANDL_API_KEY = 'AwSxXCHEuNcMv_fUohpT'
# This is to prompt you to change the Quandl Key
if QUANDL_API_KEY == 'REPLACE-THIS-TEXT-WITH-A-REAL-API-KEY':
 raise Exception("Please provide a valid Quandl API key!")
# Set the start and end date
start_date = '1990-01-01'
end_date = '2018-03-27'
# Set the ticker name
ticker = 'INFO'
# Feth the data
data = quandl.get('WIKI/'+ticker, start_date=start_date,end_date=end_date, api_key=QUANDL_API_KEY)['Adj. Close']

#Historical Logs Returns
log_returns = np.log(1 + data.pct_change()) #padas.pct_change obtains simple return from the previous dataset.

ax=data.plot(figsize=(10,6),title='IHS MARKIT Historical Share Price')
ax.set_xlabel("Price")
ax.set_ylabel("Date")

ax1=log_returns.plot(figsize=(10,6),title='IHS MARKIT Log Returns')
ax1.set_xlabel("Deviation")
ax1.set_ylabel("Date")

u= log_returns.mean()
print(u)
var= log_returns.var()
print(u)
drift= u -(0.5* var)

drift=np.array(drift)

stdev = log_returns.std()

stdev = log_returns.std() * 250 ** 0.5

norm.ppf(0.96) # allow us to obtain Z corresponds to the distance between the mean and the events, expressed as the number of standard deviations
Z=norm.ppf(np.random.rand(10,2))

t_intervals=1000
iteration=10

daily_return =np.exp(drift.values+stdev.values*norm.ppf(np.random.rand(t_intervals,iteration)))

S0=data.iloc[-1]

price_list=np.zeros_like(daily_return)
price_list[0]=S0

for t in range (1,t_intervals):
    price_list[t]= price_list[t-1]*daily_return[t]


plt.figure(figsize=(10,6))
plt.plot(price_list)



