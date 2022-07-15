
import header_handler
import binascii
import constants
import suite_helper
import Crypto.Util.Padding as padder
from Crypto.Hash import HMAC
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes


#Perform the encryption operation after collecting essential parameters
def file_ecncrypt(filename: str, password: str, iterations: int, algoForHashing: str , cipher: str):

    #open file and get the content in bytes format
    with open(filename, "rb") as f:
        byteFile_for_encrypt = f.read()

    #Extract block size and key size from cipher type
    blockSize_KeySize = suite_helper.get_blocksize_keysize_from_cipher(cipher)

    # random salt generation for masterkey, hmac_key and encryption key
    master_key_salt = binascii.hexlify(get_random_bytes(constants.SALT_SIZE)).decode()
    hmac_key_salt = binascii.hexlify(get_random_bytes(constants.SALT_SIZE)).decode()
    encryption_key_salt = binascii.hexlify(get_random_bytes(constants.SALT_SIZE)).decode()

    
    #Generate master keys, encryption key and hmac key using the PBDKF2 library
    master_key_intermediate = PBKDF2(password, master_key_salt, blockSize_KeySize[1], count = iterations, hmac_hash_module = suite_helper.hashType(algoForHashing))
    master_key = binascii.hexlify(master_key_intermediate).decode()

    encryption_key_intermediate = PBKDF2(master_key, encryption_key_salt, blockSize_KeySize[1], count = 1, hmac_hash_module = suite_helper.hashType(algoForHashing))
    encryption_key= binascii.hexlify(encryption_key_intermediate).decode()
    
    hmac_key_intermediate = PBKDF2(master_key, hmac_key_salt, blockSize_KeySize[1], count = 1, hmac_hash_module = suite_helper.hashType(algoForHashing))
    hmac_key = binascii.hexlify(hmac_key_intermediate).decode()

    #Extracting the defined cipher library
    enryption_cipher = suite_helper.cipherType(cipher, encryption_key)

    #Applyig standard padding
    padded_file = padder.pad(byteFile_for_encrypt, blockSize_KeySize[0], "pkcs7")

    #Using cipher library to do standard encryption
    encrypted_file = enryption_cipher.encrypt(padded_file)

    #combining the generated cipher file with IV
    iv_data_encryption  = enryption_cipher.iv + encrypted_file

    #Creating a HMAC
    hmac = HMAC.HMAC(binascii.unhexlify(hmac_key), iv_data_encryption, suite_helper.hashType(algoForHashing))
    hmac_iv_data_encrypted = hmac.digest() + iv_data_encryption


    #Packing encryption information into metadata
    encrypted_file_with_header =  header_handler.create_header(cipher, algoForHashing, iterations, master_key_salt, hmac_key_salt, encryption_key_salt) + constants.HEADER_SEPERATOR + hmac_iv_data_encrypted
    
    #Writing the encryption header to file and enc extension
    file_data = open(filename + constants.FILE_EXTENSION, "wb")
    file_data.write(encrypted_file_with_header)
    print("Encrypted is Complete. Encrypted file name: ", filename + constants.FILE_EXTENSION)

    

