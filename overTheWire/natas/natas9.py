#!/usr/bin/env python

from http import cookies
import requests
import re

username = 'natas9'
password = 'Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd'

# headers = {"Referer" : "http://natas5.natas.labs.overthewire.org/"}
# cookies = {"loggedin" : "1"}

url = 'http://%s.natas.labs.overthewire.org/index-source.html' % username

response = requests.get(url, auth = (username, password))
# response = requests.post(url, data = {"secret" : "oubWYf2kBq", "submit" : "submit"}, auth = (username, password))
content = response.text
print(content)
# print(re.findall('The password for natas9 is (.*)',content)[0])