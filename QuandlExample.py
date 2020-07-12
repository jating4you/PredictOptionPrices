import pandas as pd
import os
import quandl
#pd.core.common.is_list_like =pd.api.types.is_list_like
#from pandas_datareader import data
#import time
from datetime import datetime, timedelta
import matplotlib.pyplot as plt


#df=data.get_data_yahoo('MSFT','2018-01-01','2019-01-01')
#df.head()
end = datetime.now()
start = end - timedelta(days=365)
mydata2 = quandl.get('FSE/VOW3_X', start_date = start, end_date = end)
f = mydata2.reset_index()
# timeseries
plt.figure(1)
f = pd.Series(f.Close.values,f.Date)
f.plot()
plt.show()

quandl.ApiConfig.api_key  = "AwSxXCHEuNcMv_fUohpT"

data = quandl.get("WIKI/KO", trim_start = "2000-12-12", trim_end = "2014-12-30", authtoken=auth_tok)
data.describe()
#Step 1. install panda             > pip install pandas
#Step 2. install pandas_datareader > pip install pandas_datareader
#Step 3. pd.core.common.is_list_like =pd.api.types.is_list_like
#Step 4. pd.core.common.is_list_like =pd.api.types.is_list_like

print(data)