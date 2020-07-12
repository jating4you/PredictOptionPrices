from nsetools import Nse
from pprint import pprint
import csv
import pandas as pd
import ta
import math

from prettytable import PrettyTable
nse = Nse()
#dir(math)
#print(nse)
#print(nse.get_index_quote('INDIA VIX'))



def printStocks(stocks):
    Ntable = PrettyTable(
        ['Symbol', 'OpenPrice', 'HighPrice', 'LowPrice', "LTP", 'PreviousPrice', 'NetPrice',
         "TradedQuantity","TurnoverInLakhs","LastCorpAnnouncementDate","LastCorpAnnouncement",'Series'])
    Ntable.align["Symbol"] = "l"
    Ntable.align["OpenPrice"] = "r"
    Ntable.align["HighPrice"] = "r"
    Ntable.align["LowPrice"] = "r"
    Ntable.align["Ltp"] = "r"
    Ntable.align["PreviousPrice"] = "r"
    Ntable.align["TradedQuantity"] = "r"
    Ntable.align["TurnoverInLakhs"] = "r"
    Ntable.align["LastCorpAnnouncement"] = "l"


    for stock in stocks:
        Ntable.add_row([stock["symbol"],stock["openPrice"],stock["highPrice"],stock["lowPrice"],stock["ltp"],stock["previousPrice"],stock["netPrice"],stock["tradedQuantity"],
                        stock["turnoverInLakhs"],stock["lastCorpAnnouncementDate"],stock["lastCorpAnnouncement"],str(stock["series"])])
    #Ntable.sortby = "Population"
    #Ntable.reversesort = True
    print(Ntable)


def printStocks_HighLow(stocks):
    Ntable = PrettyTable(
        ['symbol', 'symbolDesc', 'value', "year", 'ltp', 'value_old',
         "dt","prev","change","pChange"])
    Ntable.align["symbol"] = "l"
    Ntable.align["symbolDesc"] = "l"
    Ntable.align["value"] = "r"
    Ntable.align["year"] = "r"
    Ntable.align["ltp"] = "r"
    Ntable.align["value_old"] = "r"
    Ntable.align["dt"] = "r"
    Ntable.align["prev"] = "r"
    Ntable.align["change"] = "r"
    Ntable.align["pChange"] = "r"


    for stock in stocks:
        Ntable.add_row([stock["symbol"],stock["symbolDesc"],stock["value"],stock["year"],stock["ltp"],stock["ltp"],stock["dt"],stock["prev"],
                        stock["change"],stock["pChange"]])
    #Ntable.sortby = "Population"
    #Ntable.reversesort = True
    print(Ntable)

def printStocks_active_monthly(stocks):
    Ntable = PrettyTable(
        ['security', 'sharetotal', 'trdQty', "nooftrades", 'avgdailyturn', 'turnover'])
    Ntable.align["security"] = "l"
    Ntable.align["sharetotal"] = "r"
    Ntable.align["trdQty"] = "r"
    Ntable.align["nooftrades"] = "r"
    Ntable.align["avgdailyturn"] = "r"
    Ntable.align["turnover"] = "r"


    for stock in stocks:
        Ntable.add_row([stock["security"],stock["sharetotal"],stock["trdQty"],stock["nooftrades"],stock["avgdailyturn"],stock["turnover"]])
    #Ntable.sortby = "Population"
    #Ntable.reversesort = True
    print(Ntable)

def printStocks_advances_declines(stocks):
    Ntable = PrettyTable(
        ['indice', 'advances', 'declines', "unchanged" ])
    Ntable.align["indice"] = "l"
    Ntable.align["advances"] = "r"
    Ntable.align["declines"] = "r"
    Ntable.align["unchanged"] = "r"
    for stock in stocks:
        Ntable.add_row([stock["indice"],stock["advances"],stock["declines"],stock["unchanged"]])
    #Ntable.sortby = "Population"
    #Ntable.reversesort = True
    print(Ntable)




top_losers = nse.get_top_losers()
top_gainers = nse.get_top_gainers()
year_high = nse.get_year_high()
year_low = nse.get_year_low()
active_monthly = nse.get_active_monthly()
advances_declines = nse.get_advances_declines()
top_fno_gainers = nse.get_top_fno_gainers()
top_fno_losers = nse.get_top_fno_losers()

print(top_fno_gainers)
print("------Gainers-----")
printStocks(top_gainers)
print("------Loser-----")
printStocks(top_losers)
print("------year_high-----")
printStocks_HighLow(year_high)
print("------active_monthly-----")
printStocks_active_monthly(active_monthly)
print("------advances_declines-----")
printStocks_advances_declines(advances_declines)

#TODO top_fno_gainers
#TODO top_fno_losers