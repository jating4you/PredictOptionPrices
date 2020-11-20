import numpy as np
import matplotlib.pyplot as plt
# For making attractive and informative statistical graph
plt.style.use('seaborn-darkgrid')


def call_payoff(sT, strike_price, premium):
    pnl = np.where(sT > strike_price, sT - strike_price, 0)
    return pnl - premium

spot_price = 900

# Call strike price and cost
strike_price = 900
premium = 20

# Stock price range at the expiration of the call
# We have defined range for the stock price at expiry as +/- 10% from spot price
# Syntax: numpy.arange(start price, stop price)
sT = np.arange(0.9*spot_price,1.1*spot_price)


payoff_long_call = call_payoff(sT, strike_price, premium)
# Plot the graph
fig, ax = plt.subplots(figsize=(8,5))
ax.spines['bottom'].set_position('zero')
ax.plot(sT,payoff_long_call,label='Call option buyer payoff')
plt.xlabel('Infosys Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()

payoff_short_call = payoff_long_call * -1.0
# Plot
fig, ax = plt.subplots(figsize=(8,5))
ax.spines['bottom'].set_position('zero')
ax.plot(sT,payoff_short_call,label='Short 940 Strike Call',color='r')
plt.xlabel('Infosys Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()


#example
# Tata motors stock price
spot_price = 430
# Stock price range at expiration of the call
sT = np.arange(0.98*spot_price, 1.03*spot_price)
# Call strike price
strike_price = 430
# Call premium paid
premium = 3
# Type your code here
def call_payoff(sT, strike_price):
    pnl = np.where(sT > strike_price, sT - strike_price, 0)
    return pnl
payoff_call=call_payoff(sT,strike_price)
print(payoff_call)

#Question Calculate the call payoff with premium by subtracting premium from call_payoff and store it in payoff_call_with_premium array.
import numpy as np
import pandas as pd
# Tata motors stock price
spot_price = 430
# Stock price range at expiration of the call
sT = np.arange(0.98*spot_price, 1.03*spot_price)
# Call strike price
strike_price = 430
# Call premium paid
premium = 3
# Call payoff without premium
payoff_call = np.where(sT > strike_price, sT - strike_price, 0)
# Call payoff with premium
# Type your code here
payoff_call-=premium
payoff_call_with_premium=payoff_call
print(payoff_call_with_premium)

#moneyness
#is the relative postion of the current price of an underlysing asset with respect
# to the strike price of an option
option-->1. IN the money
option -->2. Out of the money
#intrinsic value
#time value of option
#put call parity
