import sys
import urllib
import urllib2
import urlparse
import requests
import hashlib
import string

def isValidURL(url):

    result = urlparse.urlparse(url)
    if (result.scheme == 'http' or result.scheme == 'https') and result.hostname != None:
        return result
    else:
        return -1

def getLongURL(url):
    return urllib.urlencode({"longurl": url})

def hashURL(netloc):
    hashedURL = hashlib.md5()
    hashedURL.update(netloc)
    return str(hashedURL.hexdigest()[:5])

def appendDomainName(hashedOutput):
    domain = 'jwang.com/'
    shortenedLink = domain + (str(hashedOutput))
    print shortenedLink

def main():

    s = requests.session()
    url = str(sys.argv[1])
    validURL = isValidURL(url)
    if validURL == -1:
        return
    validURL = validURL.netloc.replace("www.","")
    hashedOutput = hashURL(validURL)
    appendDomainName(hashedOutput)
    print s

main()
