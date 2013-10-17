import sys
import urlparse
import hashlib
import re

def isValidURL(url):

    result = urlparse.urlparse(url)

    # if missing http(s), append to beginning of URL
    if (result.scheme != 'http' or result.scheme != 'https') and result.hostname == None and result.path != None:
        url = 'http://' + url
        result = urlparse.urlparse(url)

    hostname = result.netloc.replace("www.","") # take out 'www.' so it doesn't get hashed
    match = re.search('.+\..+',hostname) # check if valid URL

    if match:
        return hostname+result.path+result.params+result.query+result.fragment
    else:
        print "Error: not a valid URL"
        return -1


def hashURL(validURL):
    hashedURL = hashlib.md5()
    hashedURL.update(validURL)
    return str(hashedURL.hexdigest()[:5])

def appendDomainName(hashedOutput):
    domain = 'jwang.com/'
    shortenedLink = domain + (str(hashedOutput))
    return shortenedLink

def main():

    if len(sys.argv) != 2:
        print "Error: invalid input"
        return
        
    url = str(sys.argv[1])
    validURL = isValidURL(url)

    if validURL == -1:
        return

    hashedOutput = hashURL(validURL)
    shortenedURL = appendDomainName(hashedOutput)
    print shortenedURL

main()
