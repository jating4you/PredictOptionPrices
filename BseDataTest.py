from bsedata.bse import BSE
import urllib.request
b = BSE()
print(b)
# Output:
# Driver Class for Bombay Stock Exchange (BSE)

# to execute "updateScripCodes" on instantiation
b = BSE(update_codes = True)
q = b.getQuote('534976')
print(q)

contents = urllib.request.urlopen("https://www.bseindia.com/stock-share-price/reliance-industries-ltd/reliance/500325/")
print(contents)