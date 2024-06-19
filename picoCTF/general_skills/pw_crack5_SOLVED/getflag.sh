#!/usr/bin/bash
python3 level5.py | grep -ioE 'picoCTF{.*?}' --color=none
