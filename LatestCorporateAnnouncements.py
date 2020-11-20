# https://api.bseindia.com/BseIndiaAPI/api/AnnGetData/w?strCat=-1&strPrevDate=20200914&strScrip=&strSearch=P&strToDate=20200914&strType=C
# Parse a JSON response using Python requests library

import requests
from requests.exceptions import HTTPError

try:
    response = requests.get(
        'https://api.bseindia.com/BseIndiaAPI/api/AnnGetData/w?strCat=-1&strPrevDate=20200914&strScrip=&strSearch=P&strToDate=20200914&strType=C')
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    print("Entire JSON response")
    print(jsonResponse)
    print("Print each key-value pair from JSON response")
    for key, value in jsonResponse.items():
        print(key, ":", value)
        print("Access directly using a JSON key name")
    print("URL is ")
    print(jsonResponse["url"])


except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')

