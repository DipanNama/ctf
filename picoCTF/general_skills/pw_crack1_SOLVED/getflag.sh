#!/usr/bin/bash
echo '1e1a' | python3 level1.py | grep -ioE 'picoCTF{.*?}' --color=none
