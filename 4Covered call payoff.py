import numpy as np
import matplotlib.pyplot as plt
# For making an attractive and informative statistical graph
plt.style.use('seaborn-darkgrid')

def call_payoff(sT, strike_price, premium):
    return np.where(sT > strike_price, sT - strike_price, 0) - premium

# Wipro stock price
spot_price = 300

# Short call
strike_price_short_call = 300
premium_short_call = 10
# Stock price range at expiration of the call
sT = np.arange(0.9*spot_price,1.1*spot_price,1)
payoff_wipro_stock = sT-300
payoff_short_call = call_payoff(sT, strike_price_short_call, premium_short_call) * -1.0
covered_call_payoff = payoff_wipro_stock + payoff_short_call
# Plot
fig, ax = plt.subplots(figsize=(8,5))
ax.spines['bottom'].set_position('zero')
ax.plot(sT,payoff_wipro_stock,'--',label='Long Wipro Stock',color='g')
ax.plot(sT,payoff_short_call,'--',label='Short 300 Strike Call ',color='r')
ax.plot(sT,covered_call_payoff,label='Covered Call')
plt.xlabel('Wipro Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()