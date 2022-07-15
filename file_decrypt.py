
import header_handler
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Hash import HMAC
import binascii
import suite_helper
from Crypto.Util.Padding import unpad
import constants

def file_decrypt(filename: str, password: str):
    
    #open file and get the content in bytes format
    with open(filename, "rb") as f:
        file_data = f.read()

    #extract and unwrap the header to gather encoding information
    cipher,algoForHashing,iterations,master_key_salt,hmac_key_salt ,encryption_key_salt = header_handler.unwrap_header(file_data)

    #Extract block size and key size from cipher type
    blockSize_KeySize = suite_helper.get_blocksize_keysize_from_cipher(cipher)

    #Generate master keys, encryption key and hmac key using the PBDKF2 library
    master_key_intermediate = PBKDF2(password, master_key_salt, blockSize_KeySize[1], count = iterations, hmac_hash_module = suite_helper.hashType(algoForHashing))
    master_key = binascii.hexlify(master_key_intermediate).decode()

    decryption_key_intermediate = PBKDF2(master_key, encryption_key_salt, blockSize_KeySize[1], count = 1, hmac_hash_module = suite_helper.hashType(algoForHashing))
    decryption_key= binascii.hexlify(decryption_key_intermediate).decode()
    
    hmac_key_intermediate = PBKDF2(master_key, hmac_key_salt, blockSize_KeySize[1], count = 1, hmac_hash_module = suite_helper.hashType(algoForHashing))
    hmac_key = binascii.hexlify(hmac_key_intermediate).decode()

    #get the file content
    hmac_encrypted_data = header_handler.get_payload(file_data)

    #Extract HMAC
    hmac_extracted = hmac_encrypted_data[0:suite_helper.hashType(algoForHashing).digest_size]

    #Extract IV, data encryption and derive HMAC
    iv_data_encrypted = hmac_encrypted_data[suite_helper.hashType(algoForHashing).digest_size:]
    iv = iv_data_encrypted[:blockSize_KeySize[0]]
    data_encrypted = iv_data_encrypted[len(iv):]
    hmac_derived = HMAC.HMAC(binascii.unhexlify(hmac_key), iv_data_encrypted, suite_helper.hashType(algoForHashing))

    #Validate HMAC
    if hmac_derived.digest() != hmac_extracted:
        raise ValueError("Invalid data to decrypt.")

    #Chosing a cipher module and creating an cipher object based cipher type, decryption key and IV 
    dec_cipher = suite_helper.decryptCipherType(cipher,decryption_key,iv)
    
    #Extracting raw decypted data
    data_decrypted = dec_cipher.decrypt(data_encrypted)

    #unpadding based on  blocksize and standards
    unpad(data_decrypted, blockSize_KeySize[0], "pkcs7")

    #Writing the decrypted data to a file, modifying the filename and adding extension
    with open(constants.FILE_PREFIX + filename[0:-len(constants.FILE_EXTENSION)], "wb") as fw:
        fw.write(data_decrypted)
    
    print("Decryption is Completed. Decrypted File name: ", constants.FILE_PREFIX + filename[0:-len(constants.FILE_EXTENSION)])