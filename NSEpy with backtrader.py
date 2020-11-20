#https://swapniljariwala.github.io/2017/11/03/NSEPy-with-backtrader.html
#%matplotlib inline
from datetime import date
import pandas as pd
from nsepy import get_history
from nsepy import get_index_pe_history

try:
    nifty = pd.read_csv('data/nifty17years_withPE.csv')
    print('Read from disk successful')
except:
    print('Downloading from NSE')
    nifty = get_history('NIFTY', date(2000, 1, 1), date.today(), index=True)
    pe = get_index_pe_history('NIFTY', date(2000, 1, 1), date.today())
    nifty['PE'] = pe['P/E']
    nifty.to_csv('data/nifty17years_withPE.csv')
    print(nifty)

from backtrader.feeds import GenericCSVData


# Define the new parameter
class GenericCSV_PE(GenericCSVData):
    # Add a 'pe' line to the inherited ones from the base class
    lines = ('pe',)

    # add the parameter to the parameters inherited from the base class
    params = (('pe', 8),)


# Declare position of each column in csv file
data = GenericCSV_PE(dataname='data/nifty17years_withPE.csv',
                     dtformat=('%Y-%m-%d'),
                     datetime=0,
                     high=1,
                     low=2,
                     open=3,
                     close=4,
                     volume=5,
                     pe=7,
                     openinterest=-1,
                     # fromdate=date(2017,1,1),
                     # todate=date(2017,1,10)
                     )
import backtrader as bt


class PEInvesting(bt.SignalStrategy):
    def log(self, txt, dt=None):
        pass

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        self.pe = self.datas[0].pe

    def next(self):
        curdate = self.datetime.date(ago=0)

        if self.pe[0] < 21:
            self.log(self.dataclose[0])
            # Use 100% of the cash to buy nifty
            self.order_target_percent(target=1.0)

        if self.pe[0] > 24:
            self.log(self.dataclose[0])
            # Sell everything
            self.order_target_percent(target=0)

cerebro = bt.Cerebro()

# Set our desired cash start
cerebro.broker.setcash(1000000.0)
cerebro.adddata(data)

cerebro.addstrategy(PEInvesting)
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
print('Final value is %.2f times the initial investment'%(cerebro.broker.getvalue()/1000000.0))
cerebro.plot()