import numpy as np
import matplotlib.pyplot as plt
# For making an attractive and informative statistical graph
plt.style.use('seaborn-darkgrid')


def call_payoff(sT, strike_price, premium):
    return np.where(sT > strike_price, sT - strike_price, 0) - premium

## Define parameters

spot_price = 900

# Long call
strike_price_long_call = 920
premium_long_call = 15

# Short call
strike_price_short_call = 940
premium_short_call = 10

# Stock price range at expiration of the call
sT = np.arange(0.95*spot_price,1.1*spot_price,1)
## Long 920 strike call payoff
payoff_long_call = call_payoff(sT, strike_price_long_call, premium_long_call)
# Plot
fig, ax = plt.subplots(figsize=(8,5))
ax.spines['bottom'].set_position('zero')
ax.plot(sT,payoff_long_call,label='Long 920 Strike Call',color='g')
plt.xlabel('Infosys Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()
## Short 940 strike call payoff
payoff_short_call = call_payoff(sT, strike_price_short_call, premium_short_call) * -1.0
# Plot
fig, ax = plt.subplots(figsize=(8,5))
ax.spines['bottom'].set_position('zero')
ax.plot(sT,payoff_short_call,label='Short 940 Strike Call',color='r')
plt.xlabel('Infosys Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()

##Bull call spread payoff
payoff_bull_call_spread = payoff_long_call + payoff_short_call

print ("Max Profit:", max(payoff_bull_call_spread))
print ("Max Loss:", min(payoff_bull_call_spread))

# Plot
fig, ax = plt.subplots(figsize=(8,5))
ax.spines['bottom'].set_position('zero')
ax.plot(sT,payoff_long_call,'--',label='Long 920 Strike Call',color='g')
ax.plot(sT,payoff_short_call,'--',label='Short 940 Strike Call ',color='r')
ax.plot(sT,payoff_bull_call_spread,label='Bull Call Spread')
plt.xlabel('Infosys Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()