# The following piece of code is obtained from urllib3 documentation webpage.
# https://urllib3.readthedocs.io/en/latest/
# To do - I need to include this in the main logic.
import urllib3.request

def connection_status():
    try:
        http = urllib3.PoolManager()
        r = http.request('GET', 'http://httpbin.org/robots.txt')
        if r.status == 200:
            return True
    except :
        return False