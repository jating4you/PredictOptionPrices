import os

from datetime import datetime
import pandas_datareader.data as web
import pandas as pd
import pandas_datareader as dr

#f = web.DataReader("AAPL", "av-daily", start=datetime(2017, 2, 9), end=datetime(2017, 5, 24), api_key=os.getenv('pk_c268845653bf4b64bed8ff3a0052ede2 '))
#EF5GTSBYWRUSV9KP
data=dr.get_data_yahoo('ibm',start=datetime(2017, 2, 9), end=datetime(2017, 5, 24))
print(data.head())

#f = web.DataReader("AAPL", "av-daily", start=datetime(2017, 2, 9), end=datetime(2017, 5, 24), api_key=os.getenv('EF5GTSBYWRUSV9KP'))
