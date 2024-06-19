#!/usr/bin/bash
grep -ioRE 'picoCTF{.*?}' . | cut -d ":" -f2
