import sys
import urllib
import urlparse

def isValidURL(url):

    result = urlparse.urlparse(url)
    if (result.scheme == 'http' or result.scheme == 'https') and result.hostname != None:
        return result
    else:
        return -1

def getLongURL(url):
    return urllib.urlencode({"longurl": url})

def main():

    url = str(sys.argv[1]);
    if isValidURL(url) == -1:
        return
    longURL = getLongURL(url);
    print longURL

main()
