import sys
import hashlib
import re

def http_check(url):

    if not url.startswith(('http://','https://')):
        url = 'http://' + url

    return url

def is_valid_url(url):

    match = re.search('.+\..+',url)

    if match:
        return 1
    else:
        return -1


def hash_url(url):
    hashed_url = hashlib.md5()
    hashed_url.update(url)
    return str(hashed_url.hexdigest()[:5])

def shorten_url(long_url):
    long_url = http_check(long_url)
    is_valid = is_valid_url(long_url)

    if is_valid == -1:
        return
    else:
        hashed_output = hash_url(long_url)
        shortened_url = 'jwang.com/' + (str(hashed_output))
        return shortened_url

def main():
    if len(sys.argv) != 2:
        print "Error: invalid input"
        return
        
    url = str(sys.argv[1])
    result = shorten_url(url)
    print result
    return
    
if __name__ == '__main__':
    main()
