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
end_date = '2018-03-01'
# Set the ticker name
ticker = 'INFO'#IHS MARKIT
# Feth the data
data = quandl.get('WIKI/'+ticker, start_date=start_date,end_date=end_date, api_key=QUANDL_API_KEY)['Adj. Close']

print(data.head())
log_returns = np.log(1 + data.pct_change())

log_returns=log_returns.dropna()
print('Log Return')
print(log_returns)
stdev = log_returns.std() * 250 ** 0.5

r = 0.025
T = 1.0
t_intervals = 250
delta_t = T / t_intervals

iterations = 10000

Z = np.random.standard_normal((t_intervals + 1, iterations))
S = np.zeros_like(Z)
S0 = data.iloc[-1]
S[0] = S0
for t in range(1, t_intervals + 1):
    S[t] = S[t-1] * np.exp((r - 0.5 * stdev ** 2) * delta_t + stdev * delta_t ** 0.5 * Z[t])

plt.figure(figsize=(10, 6))
plt.plot(S[:, :10]);
plt.show()
print(log_returns)

