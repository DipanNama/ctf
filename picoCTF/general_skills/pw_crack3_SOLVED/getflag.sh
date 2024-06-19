#!/usr/bin/bash
python3 level3.py | grep -ioE 'picoCTF{.*?}' --color=none
