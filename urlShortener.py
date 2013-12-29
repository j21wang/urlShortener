import sys
import hashlib
import re
import requests
import math

def prepend_http(url):
    if not url.startswith(('http://','https://')):
        url = 'http://' + url

    return url

def is_valid_url(url):
    return re.match('https?://.+\..+',url)

def encode(url):
    print url
    chars = "\/\.0123456789abcdefghijklmnopqrstuvwxyz"
    alnum_url = url.lower()
    alnum_url = re.sub("^https?://","",alnum_url)
    
    short_url = ""
    for char in alnum_url:
        num = chars.find(char)
        num = num + 1 # 5 was chosen for funsies
        short_url = short_url + chars[num]

    return short_url

def decode(url):
    chars = "\/\.0123456789abcdefghijklmnopqrstuvwxyz"
    url = re.sub("^.*jwang.com/","",url)
    url = url.lower()
    
    long_url = "" 
    for char in url:
        num = chars.find(char)
        num = num - 5
        long_url = long_url + chars[num]
        
    print long_url
    return long_url

def shorten_url(long_url):
    long_url = prepend_http(long_url)
    is_valid = is_valid_url(long_url)

    if is_valid == None:
        raise Exception("Not a valid URL!")
    else:
        print long_url
        hashed_output = encode(long_url)
        shortened_url = 'jwang.com/' + (str(hashed_output))
        return shortened_url

def main():
    s = requests.Session()
    if len(sys.argv) != 2:
        print "Error: invalid input"
        return
        
    url = str(sys.argv[1])
    print url

    if re.match('(https?://)?jwang.com/.+',url):
        decode(url)
    else:
        result = shorten_url(url)
        if result != None:
            print result
    
if __name__ == '__main__':
    main()
