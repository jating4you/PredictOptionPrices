from nsepy import get_history
from nsepy.history import get_price_list
from datetime import date
from nsepy import get_index_pe_history
import matplotlib.pyplot as plt
import pandas as pd
data = get_history(symbol="SBIN", start=date(2015,1,1), end=date(2015,1,31))
data[['Close']].plot()
sbin = get_history(symbol='SBIN',
                   start=date(2020,8,1),
                   end=date(2020,9,10))
print( sbin )
print( sbin.columns )

ax = plt.gca()

sbin.plot(kind='line',x='%Deliverble',y='Date',ax=ax)
#df.plot(kind='line',x='name',y='num_pets', color='red', ax=ax)

#plt.show()
stock_opt = get_history(symbol="SBIN",
                        start=date(2020,9,1),
                        end=date(2020,9,10),
                        option_type="CE",
                        strike_price=300,
                        expiry_date=date(2015,1,29))

prices = get_price_list(dt=date(2020,9,8))
print(prices)
nifty_pe = get_index_pe_history(symbol="NIFTY",
                                start=date(2020,9,1),
                                end=date(2020,9,10))
print(nifty_pe)



from nsepy import get_rbi_ref_history
rbi_ref = get_rbi_ref_history(date(2015,1,1), date(2020,10,10))
print(rbi_ref)