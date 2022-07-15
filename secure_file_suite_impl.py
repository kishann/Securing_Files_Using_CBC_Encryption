import file_encrypt
import file_decrypt
import read_inputs
import time

if __name__ == '__main__':

    inp_obj = read_inputs.Read_inputs()
    inp_obj.gui_encrypt()
    filename, password, itr, algoHash, cipher = inp_obj.getEncryptionInputs()

    start = time.perf_counter()
    file_encrypt.file_ecncrypt(filename, password, itr, algoHash, cipher)
    end  = time.perf_counter()
    encrypt_latency = end - start
    print("Number of iterations: ", itr)
    print("Encryption latency: " + str(encrypt_latency) + " " + "seconds")

    inp_obj.gui_decrypt()
    decryptFilename, decryptPassword = inp_obj.getDecryptionInputs()

    file_decrypt.file_decrypt(decryptFilename, decryptPassword)

