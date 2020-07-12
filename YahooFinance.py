#pip install yfinance --upgrade --no-cache-dir
#https://aroussi.com/post/python-yahoo-finance
import yfinance as yf

#msft = yf.Ticker("INFO")
msft = yf.Ticker("RELIANCE.NS")

print(msft.history(period="1mo").head)


# get stock info
msft.info

# get historical market data
msft.history(period="max")

# show actions (dividends, splits)
msft.actions
# show dividends
msft.dividends