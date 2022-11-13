#!/usr/bin/env python

from http import cookies
import requests
import re

username = 'natas8'
password = 'a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB'

# headers = {"Referer" : "http://natas5.natas.labs.overthewire.org/"}
# cookies = {"loggedin" : "1"}

url = 'http://%s.natas.labs.overthewire.org/' % username

# response = requests.get(url, auth = (username, password))
response = requests.post(url, data = {"secret" : "oubWYf2kBq", "submit" : "submit"}, auth = (username, password))
content = response.text
# print(content)
print(re.findall('The password for natas9 is (.*)',content)[0])