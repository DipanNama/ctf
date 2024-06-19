#!/usr/bin/bash
python3 level4.py | grep -ioE 'picoCTF{.*?}' --color=none
