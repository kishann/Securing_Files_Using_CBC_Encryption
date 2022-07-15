
import constants
import binascii
from Crypto.Hash import SHA256
from Crypto.Hash import SHA512

from Crypto.Cipher import AES
from Crypto.Cipher import DES3

#Function to gather block size and key size based on cipher type
def get_blocksize_keysize_from_cipher(cipher: str):
    cipher_type = cipher[:3]
    cipher_length = cipher[3:]
    blockSize_KeySize = []

    if cipher_type=="AES":
        blockSize_KeySize.append(constants.AES_BLOCK)
    else:
        blockSize_KeySize.append(constants.DES_BLOCK)
    

    if cipher_type == "AES":
        if cipher_length == "128":
            blockSize_KeySize.append(16)
        else:
            blockSize_KeySize.append(32)
    else:
        blockSize_KeySize.append(24)

    return blockSize_KeySize

#Function to get the Hash module based on input hash string
def hashType(algoForHashing):

    if algoForHashing=="SHA256":
        return SHA256
    else:
        return SHA512

#Function to create a new cipher based on input cipher string 
def cipherType(cipher, key):
    if cipher[:3] == "AES":        
        return AES.new(key = binascii.unhexlify(key),mode=AES.MODE_CBC)
    else:
        return DES3.new(key = binascii.unhexlify(key),mode=DES3.MODE_CBC)

#Function to create a cipher for decryption based on cipher type, key and IV
def decryptCipherType(cipher, key, iv):
    if cipher[:3] == "AES":
        return AES.new(key=binascii.unhexlify(key), mode=AES.MODE_CBC, iv=iv)
    else:
        return DES3.new(key = binascii.unhexlify(key),mode=DES3.MODE_CBC, iv=iv)