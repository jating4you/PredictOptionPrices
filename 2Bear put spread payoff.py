import numpy as np
import matplotlib.pyplot as plt
# For making attractive and informative statistical graph
plt.style.use('seaborn-darkgrid')
def put_payoff(sT, strike_price, premium):
    return np.where(sT < strike_price, strike_price - sT, 0) - premium

# Infosys stock price
spot_price = 900
# Long put
strike_price_long_put = 880
premium_long_put = 15
# Short put
strike_price_short_put = 860
premium_short_put = 10
# Stock price range at expiration of the put
sT = np.arange(0.9*spot_price,1.05*spot_price,1)
payoff_long_put = put_payoff(sT, strike_price_long_put, premium_long_put)
payoff_short_put = put_payoff(sT, strike_price_short_put, premium_short_put) * -1.0
payoff_bear_put_spread = payoff_long_put + payoff_short_put
# Plot
fig, ax = plt.subplots(figsize=(8,5))
ax.spines['bottom'].set_position('zero')
ax.plot(sT,payoff_long_put,'--',label='Long 880 Strike Put',color='g')
ax.plot(sT,payoff_short_put,'--',label='Short 860 Strike Put',color='r')
ax.plot(sT,payoff_bear_put_spread,label='Bear Put Spread')
plt.xlabel('Infosys Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()