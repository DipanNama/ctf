#!/usr/bin/python3

from scapy.all import *

capture = rdpcap('shark1.pcapng')
for packet in capture:
	print(packet.show())