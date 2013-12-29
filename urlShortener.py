import sys
import hashlib
import re
def prepend_http(url):
    if not url.startswith(('http://','https://')):
        url = 'http://' + url

    return url

def is_valid_url(url):
    return re.match('https?://.+\..+',url)

def hash_url(url):
    hashed_url = hashlib.md5()
    hashed_url.update(url)
    #return str(hashed_url.hexdigest()[:5])
    return str(hashed_url.hexdigest())

def shorten_url(long_url):
    long_url = prepend_http(long_url)
    is_valid = is_valid_url(long_url)

    if is_valid == None:
        raise Exception("Not a valid URL!")
    else:
        hashed_output = hash_url(long_url)
        shortened_url = 'jwang.com/' + (str(hashed_output))
        return shortened_url

def main():
    if len(sys.argv) != 2:
        print "Error: invalid input"
        return
        
    url = str(sys.argv[1])

    if re.match('(https?://)?jwang.com',url):
        print 'check backwards!';

    result = shorten_url(url)

    if result != None:
        print result
    
if __name__ == '__main__':
    main()
