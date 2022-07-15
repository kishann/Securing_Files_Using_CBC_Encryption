import binascii
HEADER_SEPERATOR = b"***"
HEADER_DELIMITER = b"~"

#Function to unwrap the metadata from header
def unwrap_header(metadata: bytes):
    header_parts = metadata.split(HEADER_SEPERATOR)
    header_bytes = binascii.unhexlify(header_parts[0])
    header_data_parts = header_bytes.split(HEADER_DELIMITER)
    cipher = header_data_parts[0].decode()
    algoForHashing = header_data_parts[1].decode()
    iterations = int(header_data_parts[2])
    master_key_salt = header_data_parts[3].decode()
    hmac_key_salt = header_data_parts[4].decode()
    encryption_key_salt = header_data_parts[5].decode()

    return cipher,algoForHashing,iterations,master_key_salt,hmac_key_salt ,encryption_key_salt

#Function to get the file content payload
def get_payload(data:bytes):
    return data.split(HEADER_SEPERATOR)[1]

#Chaining metadata into a header string using a seperator
def create_header(cipher: str, algoForHashing: str, iterations: int, master_key_salt: str, hmac_key_salt : str, encryption_key_salt: str):
    header_combined_str = "~".join([cipher, algoForHashing, str(iterations), master_key_salt, hmac_key_salt, encryption_key_salt])
    header = binascii.hexlify(header_combined_str.encode())
    return header

