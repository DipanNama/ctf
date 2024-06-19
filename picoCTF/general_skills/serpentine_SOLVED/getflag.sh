#!/usr/bin/bash
echo 'b' | python3 serpentine.py 2>/dev/null | grep -ioE 'picoCTF{.*?}' --color=none
