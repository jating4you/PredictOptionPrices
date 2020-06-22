from nsetools import Nse
from pprint import pprint
nse = Nse()
print(nse)
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
            print(stock["symbol"],":",str(stock["ltp"]),"gain",gainorloss)
        elif gainorloss<=0:
            print(stock["symbol"], ":", str(stock["ltp"]), "loss", gainorloss)
top_losers = nse.get_top_losers()
top_gainers = nse.get_top_gainers()
print("------Gainers-----")
printStocks(top_gainers)
print("------Loser-----")
printStocks(top_losers)
mylist= ['ADANIGREEN','ALOKTEXT','ANDHRAPET','ASHOKA','ASHOKLEY','AXISBANK','BANKBARODA','BEL','BHEL','BILENERGY','BIOCON','CADILAHC','COX&KINGS','CPSEETF','DHANBANK','DISHTV','EDELWEISS','ENGINERSIN','EQUITAS','EVEREADY','EXELINDUS','FSL','GAIL','GOLDBEES','GVKPIL','HCG','HDFCBANK','HDFCLIFE','ICICIBANK','ICICINIFTY','ICICINV20','ICICINXT50','IDFCFIRSTB','INDUSINDBK','INSECTICID','IOB','IOC','IRCON','ITI','J&KBANK','JAICORPLTD','JUNIORBEES','KSCL','KSK-BE','L&TFH','LT','MIDHANI','NAM-INDIA','NBCC','NEWGEN','NHPC','NTPC','PCJEWELLER','PFC','PIDILITIND','PNB','RALLIS','RCOM','RUCHI','RVNL','SBICARD','SBILIFE','SBIN','STARCEMENT','STRTECH','SUNPHARMA','SUPRAJIT','SUZLON','TATACHEM','TINPLATE','TRIDENT','TV18BRDCST','UCOBANK','UJAAS','UNIPLY','VIKASPROP']
for stockName in mylist:
    if nse.is_valid_code(stockName):
        stock= nse.get_quote(stockName)

        print(stock['symbol'],":",str(stock["lastPrice"]),"gain/lose",":",str(float(stock['change'])/stock['basePrice'] *100))

#print(top_gainers['BAJFINANCE'])
#nse.is_valid_code('infy')
#nse.is_valid_code('innnfy')
#nse.get_fno_lot_sizes()