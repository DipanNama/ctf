#!/usr/bin/bash
cat index.html | grep -ioE 'picoCTF{.*?}' --color=none
