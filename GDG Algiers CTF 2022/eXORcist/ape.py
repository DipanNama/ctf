#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Dipan Nama
# @Date:   2022-10-09 01:39:10
# @Last Modified by:   Dipan Nama
# @Last Modified time: 2022-10-09 02:19:16


import random

message = b'\xc3\xb8v\xc3\xaf\xc2\x98I\xc3\x8e\xc2\x92\xc3\xb2R\xc2\x88#\xc3\xa3\xc3\xb0\x1c\xc2\x8c\x11\xc3\xbcr\xc3\xb6\xc2\x81S\xc3\x94\xc2\x88\xc3\xa8'
FLAG=b'XXXXXXXXXXXXXXXXXXXX'
# xor_of_MESSAGE_and_OFFSET = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'


def xor(message, key):
    return ''.join([chr(m^k) for m,k in zip(message, key)] )


offset = random.randint(0, len(message))

i=0

while True:
    offset_for_decoding = random.randint(0, len(message))
    new_offset_value_for_decoding = (message[:offset]+FLAG+message[offset:])
    print(f"OFFSET | {new_offset_value_for_decoding}") 
    print()

    print("XORING BETWEEN new_offset_value_for_decoding AND message")
    print()

    xor_of_MESSAGE_and_OFFSET_NEW_FOR_DECODING = xor(message,new_offset_value_for_decoding).encode() # OFFSET && MESSAGE = KEY
    print(f"OFFSET && MESSAGE = KEY | {xor_of_MESSAGE_and_OFFSET_NEW_FOR_DECODING}")
    print()

    print(i)
    i +=1
    if xor_of_MESSAGE_and_OFFSET == xor_of_MESSAGE_and_OFFSET_NEW_FOR_DECODING:
    	print(f"{xor_of_MESSAGE_and_OFFSET} | {xor_of_MESSAGE_and_OFFSET_NEW_FOR_DECODING}")
    	break