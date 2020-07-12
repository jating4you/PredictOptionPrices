from nsetools import Nse
from pprint import pprint
import csv
import pandas as pd
import ta

# Load datas
df = pd.read_csv('datas.csv', sep=',')

# Clean NaN values
df = ta.utils.dropna(df)
indicator_bb = ta.volatility.BollingerBands(close=df["Close"], n=20, ndev=2)
# Add Bollinger Bands features
df['bb_bbm'] = indicator_bb.bollinger_mavg()
df['bb_bbh'] = indicator_bb.bollinger_hband()
df['bb_bbl'] = indicator_bb.bollinger_lband()

# Add Bollinger Band high indicator
df['bb_bbhi'] = indicator_bb.bollinger_hband_indicator()

# Add Bollinger Band low indicator
df['bb_bbli'] = indicator_bb.bollinger_lband_indicator()

# Add ta features filling NaN values
df = ta.add_all_ta_features(
    df, open="Open", high="High", low="Low", close="Close", volume="Volume_BTC", fillna=True)
#print(df)

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
    print("Total no. of rows: %d" % (csvreader.line_num))

# printing the field names
#print('Field names are:\n' + ', '.join(field for field in fields))
investment=0
totalinvestment=0
for row in rows[:]:
	# parsing each column of a row
    investment= float(row[1])*float(row[2])
    totalinvestment+=investment
    print(row[0],row[1],row[2],investment)

print("-------Total Investment---------",totalinvestment)

nse = Nse()
print(nse)
data=nse.download_bhavcopy("24th Jun")
print(data)

#https://nsetools.readthedocs.io/en/latest/usage.html
q = nse.get_quote('ADANIGREEN')  # it's ok to use both upper or lower case for codes.
pprint(q)
#print(q.dayHigh)
#nse.get_index_list()

#nse.get_index_quote("nifty bank")
all_stock_codes = nse.get_stock_codes()
index_codes = nse.get_index_list()
#pprint(index_codes)
adv_dec = nse.get_advances_declines()
#pprint(adv_dec)


def printStocks(stocks):
    for stock in stocks:
        gainorloss= (stock["ltp"]-stock['previousPrice'])/stock['previousPrice'] *100
        if gainorloss>0:
            print(stock["symbol"],":",str(stock["ltp"]),"gain",str(gainorloss),stock["lastCorpAnnouncement"],stock["lastCorpAnnouncementDate"])
        elif gainorloss<=0:
            print(stock["symbol"], ":", str(stock["ltp"]), "loss", str(gainorloss),stock["lastCorpAnnouncement"],stock["lastCorpAnnouncementDate"])
top_losers = nse.get_top_losers()
top_gainers = nse.get_top_gainers()
print("------Gainers-----")
printStocks(top_gainers)
print("------Loser-----")
printStocks(top_losers)
print("------My Stock List-----")
mylist= ['ADANIGREEN','ALOKTEXT','ANDHRAPET','ASHOKA','ASHOKLEY','AXISBANK','BANKBARODA','BEL','BHEL','BILENERGY','BIOCON','CADILAHC','COX&KINGS','CPSEETF','DHANBANK','DISHTV','EDELWEISS','ENGINERSIN','EQUITAS','EVEREADY','EXELINDUS','FSL','GAIL','GOLDBEES','GVKPIL','HCG','HDFCBANK','HDFCLIFE','ICICIBANK','ICICINIFTY','ICICINV20','ICICINXT50','IDFCFIRSTB','INDUSINDBK','INSECTICID','IOB','IOC','IRCON','ITI','J&KBANK','JAICORPLTD','JUNIORBEES','KSCL','KSK-BE','L&TFH','LT','MIDHANI','NAM-INDIA','NBCC','NEWGEN','NHPC','NTPC','PCJEWELLER','PFC','PIDILITIND','PNB','RALLIS','RCOM','RUCHI','RVNL','SBICARD','SBILIFE','SBIN','STARCEMENT','STRTECH','SUNPHARMA','SUPRAJIT','SUZLON','TATACHEM','TINPLATE','TRIDENT','TV18BRDCST','UCOBANK','UJAAS','UNIPLY','VIKASPROP']
for stockName in mylist:
    if nse.is_valid_code(stockName):
        stock= nse.get_quote(stockName)
        gainorloss = (float(stock["change"]) / stock['basePrice'] )* 100
        if gainorloss > 0:
            print(stock["symbol"], ":", str(stock["lastPrice"]), "gain", gainorloss)
        elif gainorloss <= 0:
            print(stock["symbol"], ":", str(stock["lastPrice"]), "loss", gainorloss)

        #print(stock['symbol'],":",str(stock["lastPrice"]),"gain/lose",":",str(float(stock['change'])/stock['basePrice'] *100))

#print(top_gainers['BAJFINANCE'])
#nse.is_valid_code('infy')
#nse.is_valid_code('innnfy')
#nse.get_fno_lot_sizes()