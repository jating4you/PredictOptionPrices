from nsetools import Nse
from pprint import pprint
import csv
import pandas as pd
import ta
from sqlalchemy.sql import quoted_name
import multiprocessing
from joblib import Parallel, delayed
import multiprocessing

from prettytable import PrettyTable


table = PrettyTable(['Instrument', 'Qty.', 'Avg. cost','LTP','Cur. val','P&L','Day chg.'])

#for rec in l:
 #   table.add_row(["Jaitn ","goyal",'12'])

#print(table)

nse = Nse()
print(nse)

filename = "holdings24062020.csv"
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

    # get total number of rows
    print("Total no. of Holding: %d" % (csvreader.line_num))

# printing the field names
#print('Field names are:\n' + ', '.join(field for field in fields))
investment=0
totalinvestment=0

for row in rows[:]:
	# parsing each column of a row
    stockName=row[0]
    quantity=float(row[1])
    avgPrice=float(row[2])
    investment = quantity*avgPrice
    totalinvestment+=investment
    if nse.is_valid_code(stockName):
        nseStock = nse.get_quote(stockName)
        daychange = ((float(nseStock["change"]) / nseStock['basePrice']) * 100)
        PL=(float(nseStock["lastPrice"])-avgPrice)*quantity
        table.add_row([stockName, quantity, avgPrice,nseStock["lastPrice"],investment,PL,daychange])

print("-------Total Investment---------=",totalinvestment)
print(table)
nse = Nse()
print(nse)


def printStocks(stocks):
    for stock in stocks:
        gainorloss= (stock["ltp"]-stock['previousPrice'])/stock['previousPrice'] *100
        if gainorloss>0:
            print(stock["symbol"],":",str(stock["ltp"]),"gain",str(gainorloss),stock["lastCorpAnnouncement"],stock["lastCorpAnnouncementDate"])
        elif gainorloss<=0:
            print(stock["symbol"], ":", str(stock["ltp"]), "loss", str(gainorloss),stock["lastCorpAnnouncement"],stock["lastCorpAnnouncementDate"])


print("------My Stock List-----")
myHoldings = ['ADANIGREEN','ALOKTEXT','ANDHRAPET','ASHOKA','ASHOKLEY','AXISBANK','BANKBARODA','BEL','BHEL','BILENERGY','BIOCON','CADILAHC','COX&KINGS','CPSEETF','DHANBANK','DISHTV','EDELWEISS','ENGINERSIN','EQUITAS','EVEREADY','EXELINDUS','FSL','GAIL','GOLDBEES','GVKPIL','HCG','HDFCBANK','HDFCLIFE','ICICIBANK','ICICINIFTY','ICICINV20','ICICINXT50','IDFCFIRSTB','INDUSINDBK','INSECTICID','IOB','IOC','IRCON','ITI','J&KBANK','JAICORPLTD','JUNIORBEES','KSCL','KSK-BE','L&TFH','LT','MIDHANI','NAM-INDIA','NBCC','NEWGEN','NHPC','NTPC','PCJEWELLER','PFC','PIDILITIND','PNB','RALLIS','RCOM','RUCHI','RVNL','SBICARD','SBILIFE','SBIN','STARCEMENT','STRTECH','SUNPHARMA','SUPRAJIT','SUZLON','TATACHEM','TINPLATE','TRIDENT','TV18BRDCST','UCOBANK','UJAAS','UNIPLY','VIKASPROP']
for stockName in myHoldings:
    if nse.is_valid_code(stockName):
        stock= nse.get_quote(stockName)
        gainorloss = (float(stock["change"]) / stock['basePrice'] )* 100
        if gainorloss > 0:
            print(stock["symbol"], ":", str(stock["lastPrice"]), "gain", gainorloss)
        elif gainorloss <= 0:
            print(stock["symbol"], ":", str(stock["lastPrice"]), "loss", gainorloss)

