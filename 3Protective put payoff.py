import numpy as np
import matplotlib.pyplot as plt
# For making an attractive and informative statistical graph
plt.style.use('seaborn-darkgrid')

def put_payoff(sT, strike_price, premium):
    return np.where(sT < strike_price, strike_price - sT, 0) - premium

# Auro Pharma stock price
spot_price = 700
# Auro Pharma stock purchase price
stock_purchase_price = 700
# Short put
strike_price_long_put = 700
premium_long_put = 20
# Stock price range at expiration of the put
sT = np.arange(0.9*spot_price,1.1*spot_price,1)
payoff_long_put = put_payoff(sT, strike_price_long_put, premium_long_put)
payoff_auro_pharma_stock = sT - stock_purchase_price
payoff_protective_put = payoff_auro_pharma_stock + payoff_long_put

# Plot
fig, ax = plt.subplots(figsize=(8,5))
ax.spines['bottom'].set_position('zero')
ax.plot(sT,payoff_auro_pharma_stock,'--',label='Long Auro Pharma Stock',color='g')
ax.plot(sT,payoff_long_put,'--',label='Long 700 Strike Put',color='r')
ax.plot(sT,payoff_protective_put,label='Protective Put')
plt.xlabel('Auro Pharma Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()