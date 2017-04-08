#!/usr/bin/python


# example code using the nacl library is from:
#  https://pynacl.readthedocs.io/en/latest/public/#example
# 
# see also: https://github.com/pyca/pynacl/issues/150

import binascii 
import nacl.utils
import nacl.secret
import nacl.utils

from nacl.public import PrivateKey, Box

# this code has Bob send an encrypted message to Alice 

# Generate Bob's private key, which must be kept secret
skbob = PrivateKey.generate()

# generate a printable key, in hexadecimal format 
skbobHex = skbob.encode(encoder=nacl.encoding.HexEncoder)
print ("Bobs secret key is: %s" % (skbobHex))

# Bob's public key can be given to anyone wishing to send
# Bob an encrypted message

# the code below shows how to generate the public key in
# in Binary, convert it to a hexadecimal format and then
# convert it back into binary

# this is the Bob's public key in binary 
pkbob1 = skbob.public_key

# convert the binary key to a printable version in hexadecimal
pkbobHex = pkbob1.encode(encoder=nacl.encoding.HexEncoder)
print ("Bobs public key is: %s" % (pkbobHex))

# convert the string hex key back to the binary 
pkbob = nacl.public.PublicKey(pkbobHex, nacl.encoding.HexEncoder)
encoded_public_key = skbob.public_key.encode(encoder = nacl.encoding.HexEncoder)

try: 
    decoded_public_key = nacl.public.PublicKey(encoded_public_key, encoder = nacl.encoding.HexEncoder)
except TypeError:
    print "Error decoding the key"

# Alice does the same and then Alice and Bob exchange public keys
skalice = PrivateKey.generate()
pkalice = skalice.public_key

# Bob wishes to send Alice an encrypted message so Bob must make a Box with
#   his private key and Alice's public key
bob_box = Box(skbob, pkalice)

# This is our message to send, it must be a bytestring as Box will treat it
#   as just a binary blob of data.

# Note the "b" in the front of the string means to keep the string in
# binary/ascii format, as opposed to UTF-8 or Unicode 
message = b"This is a binary message"

# Encrypt our message, it will be exactly 40 bytes longer than the
#   original message as it stores authentication information and the
#   nonce alongside it.

# the encrypt function must take a nonce now
#encrypted = bob_box.encrypt(message)

# This is a nonce, it *MUST* only be used once, but it is not considered
#   secret and can be transmitted or stored alongside the ciphertext. A
#   good source of nonces are just sequences of 24 random bytes.
nonce = nacl.utils.random(Box.NONCE_SIZE)
encrypted = bob_box.encrypt(message, nonce)

print ("The length of the plaintext is %d and the cyphertext is %d" % (len(message),len(encrypted)))
# Alice creates a second box with her private key to decrypt the message
alice_box = Box(skalice, pkbob)

# Decrypt our message, an exception will be raised if the encryption was
#   tampered with or there was otherwise an error.
plaintext = alice_box.decrypt(encrypted)

print ("the plaintext is: %s" %(plaintext))
