#!/usr/bin/env python

from urllib import response
import requests
import re

username = 'natas1'
password = 'g9D9cREhslqBKtcA2uocGHPfMZVzeFK6'

url = 'http://%s.natas.labs.overthewire.org' % username

response = requests.get(url, auth = (username, password))
content = response.text
# print(content)
print(re.findall('<!--The password for natas2 is (.*) -->',content)[0])