import requests

def is_downloadable(url):
    """
    Does the url contain a downloadable resource
    """
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    print(header)
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True

print( is_downloadable('https://www1.nseindia.com/ArchieveSearch?h_filetype=eqbhav&date=28-08-2020&section=EQ'))
# >> False
print( is_downloadable('http://google.com/favicon.ico'))
# >> True