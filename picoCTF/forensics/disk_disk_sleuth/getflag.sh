#!/usr/bin/bash

srch_strings dds1-alpine.flag.img | grep -oE 'picoCTF{.*?}' --color=none