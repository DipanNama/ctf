#! /usr/bin/bash

cat enc_flag | base64 -d | cut -d "'" -f2 | base64 -d | rot -b | grep -ioE 'picoCTF{.*?}' --color=none
