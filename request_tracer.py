import requests
import sys    #for system related information
from subprocess import Popen, PIPE
import subprocess
import re
import json as m_json
import socket
import urllib
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse
try:
    import urllib.request       #Python 3.x
except ImportError:
    import urllib2 

def traceroute(url):
    while True:
        if 'http' not in url:
            url = "http://" + url
        elif "www" not in url:
            url = "www."[:7] + url[7:]
        else:
            url = url
            break
    url = urlparse(url)
    url = url.netloc

    # open subprocess to call traceroute in system.

    p = Popen(['traceroute', url], stdout=PIPE)
    while True:
        line = p.stdout.readline()
        if not line: break
        line2 = str(line).replace('\\r','').replace('\\n','')

        # regex to find ip in the line2
        
        pattern = r"((([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])[ (\[]?(\.|dot)[ )\]]?){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5]))"
        matchs = [match[0] for match in re.findall(pattern, line)]
        flag = []

        # locating ip address

        for i in matchs:
            if i in flag: continue
            flag.append(i)
            url = "https://ipapi.co/"
            url = url+str(i)+"/json"
            req = requests.get(url)

            try:
                if req.json()['city']!=None:
                    print req.json()['city'], req.json()['country']
            except:
                continue


usr_url = raw_input("Enter the url: ")
traceroute(usr_url)
