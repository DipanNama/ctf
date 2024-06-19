#!/usr/bin/bash

exiftool ukn_reality.jpg | grep Att | cut -d ":" -f2 | cut -d " " -f2 | base64 -d

