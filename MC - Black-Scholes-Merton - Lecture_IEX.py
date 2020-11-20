import numpy as np
import pandas as pd
from pandas_datareader import data as wb
from scipy.stats import norm


def d1(S, K, r, stdev, T):
    return (np.log(S / K) + (r + stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))


def d2(S, K, r, stdev, T):
    return (np.log(S / K) + (r - stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))

norm.cdf(0)


def BSM(S, K, r, stdev, T):
    return (S * norm.cdf(d1(S, K, r, stdev, T))) - (K * np.exp(-r * T) * norm.cdf(d2(S, K, r, stdev, T)))
ticker = 'PG'
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source='iex', start='2015-1-1', end='2017-3-21')['close']

S = data.iloc[-1]


log_returns = np.log(1 + data.pct_change())

stdev = log_returns.std() * 250 ** 0.5



r = 0.025
K = 110.0
T = 1

d1(S, K, r, stdev, T)
d2(S, K, r, stdev, T)
print(BSM(S, K, r, stdev, T))