#!/usr/bin/env python3
# Crypto challenge of eXORciste
import os 
# from flag import FLAG
import random

FLAG=b'XXXXXXXXXXXXXXXXXXXX'

def xor(message, key):
    return ''.join([chr(m^k) for m,k in zip(message, key)] )
    


def generate_key(length):
    random_seed = os.urandom(16)
    key = random_seed * (length //16) + random_seed[:(length % 16)]
    return key 



def main():
    message = "AAAABBBBCCCCDDDDEEEEFFFF".encode()
    print(f"GIVEN : MESSAGE | {message}") # i can control this part 



    key = generate_key(len(message))
    print(f"KEY | {key}") # we can't control this key
    print()

    offset = random.randint(0, len(message))
    new_offset_value = (message[:offset]+FLAG+message[offset:])
    print(f"OFFSET | {new_offset_value}") 
    print()

    print("XORING BETWEEN new_offset_value AND key")
    print()

    cipher = xor(message[:offset]+FLAG+message[offset:], key) # KEY && OFFSET = MESSAGE
    print(f"GIVEN : KEY && OFFSET = MESSAGE | {cipher.encode()}")
    print()


    print("==========================================================================")
    print()

    xor_of_MESSAGE_and_KEY = xor(message,key).encode() # MESSAGE && KEY = OFFSET
    print(f"MESSAGE && KEY = OFFSET | {xor_of_MESSAGE_and_KEY}")
    print()

    xor_of_MESSAGE_and_OFFSET = xor(message,new_offset_value).encode() # OFFSET && MESSAGE = KEY
    print(f"OFFSET && MESSAGE = KEY | {xor_of_MESSAGE_and_OFFSET}")
    print()


    print("==========================================================================")

    # while True:
    #     offset_for_decoding = random.randint(0, len(message))
    #     new_offset_value_for_decoding = (message[:offset]+FLAG+message[offset:])
    #     print(f"OFFSET | {new_offset_value_for_decoding}") 
    #     print()

    #     print("XORING BETWEEN new_offset_value_for_decoding AND message")
    #     print()

    #     xor_of_MESSAGE_and_OFFSET_NEW_FOR_DECODING = xor(message,new_offset_value_for_decoding).encode() # OFFSET && MESSAGE = KEY
    #     print(f"OFFSET && MESSAGE = KEY | {xor_of_MESSAGE_and_OFFSET_NEW_FOR_DECODING}")
    #     print()


    #     if xor_of_MESSAGE_and_OFFSET == xor_of_MESSAGE_and_OFFSET_NEW_FOR_DECODING:

    #         break


if __name__ == "__main__":
    main()


'''
KEY && OFFSET = MESSAGE

MESSAGE && KEY = OFFSET

OFFSET && MESSAGE = KEY
'''



'''
GIVEN : MESSAGE | b'AAAABBBBCCCCDDDDEEEEFFFF'
KEY | b'\xb97\xae\xd9\x0b\x8c\xd0\xb0\x11\xcb`\xa0\xb4X\xc8U\xb97\xae\xd9\x0b\x8c\xd0\xb0'

OFFSET | b'AAAABBBBCCCCDDDDEEXXXXXXXXXXXXXXXXXXXXEEFFFF'

XORING BETWEEN new_offset_value AND key

GIVEN : KEY && OFFSET = MESSAGE | b'\xc3\xb8v\xc3\xaf\xc2\x98I\xc3\x8e\xc2\x92\xc3\xb2R\xc2\x88#\xc3\xa3\xc3\xb0\x1c\xc2\x8c\x11\xc3\xbcr\xc3\xb6\xc2\x81S\xc3\x94\xc2\x88\xc3\xa8'

==========================================================================

MESSAGE && KEY = OFFSET | b'\xc3\xb8v\xc3\xaf\xc2\x98I\xc3\x8e\xc2\x92\xc3\xb2R\xc2\x88#\xc3\xa3\xc3\xb0\x1c\xc2\x8c\x11\xc3\xbcr\xc3\xab\xc2\x9cM\xc3\x8a\xc2\x96\xc3\xb6'

OFFSET && MESSAGE = KEY | b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1d\x1d\x1e\x1e\x1e\x1e'

==========================================================================
[Finished in 44ms]
'''