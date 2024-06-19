#!/usr/bin/bash
python3 -c "print(chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36))" | python3 level2.py | grep -ioE 'picoCTF{.*?}' --color=none
