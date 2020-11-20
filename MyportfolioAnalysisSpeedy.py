#! shebang line
from nsetools import Nse
from pprint import pprint
import csv
import pandas as pd
import ta
from sqlalchemy.sql import quoted_name
from joblib import Parallel, delayed
import multiprocessing
from datetime import datetime
from prettytable import PrettyTable
import collections

nse = Nse()
print(nse)
filename = "data/holdings09092020.csv"
fields = []
rows = []
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
    print(rows)
    # get total number of rows
    print("Total no. of Holding: %d" % (csvreader.line_num-1))

# printing the field names
#print('Field names are:\n' + ', '.join(field for field in fields))
investment=0
totalinvestment=0

#for row in rows[:]:
	# parsing each column of a row
    #try:
num_cores = multiprocessing.cpu_count()





def transform(row):
    stockName=row[0]
    quantity=float(row[1])
    avgPrice=float(row[2])

    currVal = quantity*avgPrice

    nse = Nse()
    if nse.is_valid_code(stockName):
        nseStock = nse.get_quote(stockName)
        #daychange = ((float(nseStock["change"]) / nseStock['basePrice']) * 100)
        PL=(float(nseStock["lastPrice"])-avgPrice)*quantity
        PL_per=(float(nseStock["lastPrice"])-avgPrice)/avgPrice *100
        exDate=nseStock["exDate"]
#       if str(exDate=='None'):
#            exDate=str("24-SEP-01")
        return [stockName, int(quantity), avgPrice, nseStock["lastPrice"], "%.2f" % currVal, "%.2f" % PL,
                    "%.2f" % PL_per, "%.2f" % float(nseStock["pChange"]), nseStock["dayHigh"],
                    nseStock["pricebandupper"],nseStock["pricebandlower"], nseStock["deliveryQuantity"],nseStock["totalTradedVolume"],nseStock["varMargin"], nseStock["high52"], nseStock["low52"], stockName +nseStock["purpose"],
                    exDate]

    else:
        ltp = row[3]
        currVal =row[4]
        PL=row[5]
        PL_per = row[6]
        dayChg = row[7]
        return [stockName, int(quantity), avgPrice, ltp, currVal, PL,PL_per,dayChg,"NA","NA","NA","NA","NA","NA","NA","NA","NA",str("24-SEP-01")]

table=Parallel(n_jobs=num_cores, verbose=0)(delayed(transform)(row)for row in rows)
Ntable = PrettyTable(['Instrument', 'Qty.', 'Avg. cost','LTP','Cur. val','Net P&L','Net P&L %','Day chg.',"dayHigh","pricebandupper","pricebandlower",
                      "deliveryQuantity","totalTradedVolume","varMargin","high52","low52","purpose","exDate"])
table=sorted(table,key=lambda x: float(x[5]))
#table=sorted(table,key=lambda date: datetime.strptime(str(date[13]), "%d-%b-%y"))
for row in table[:]:
    Ntable.add_row(row)

print(Ntable)

nseStock = nse.get_quote("TRIDENT")
print(nseStock)
#nse.get_bhavcopy_filename()

class Holding:
    filename = "data/holdings09092020.csv"
    fields = []
    rows = []
    def loadHolding(self):
        print('Loading Holding..')
        with open(filename, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            # extracting field names through first row
            fields = next(csvreader)

            # extracting each data row one by one
            for row in csvreader:
                rows.append(row)
            print(rows)
            # get total number of rows
            print("Total no. of Holding: %d" % (csvreader.line_num - 1))

def main():
    holding = Holding()
    holding.loadHolding()




#how to upgrade all package in python
#https://www.activestate.com/resources/quick-reads/how-to-update-all-python-packages/
#pip install -r requirements.txt --upgrade
#https://www1.nseindia.com/ArchieveSearch?h_filetype=eqbhav&date=28-08-2020&section=EQ