
# Software to Secure files using CBC Encryption

This security software application is used to encrypt/decrypt a file by allowing the user to choose a secret, cipher type (AES/DES), hashing algorithm (SHA256/SHA512), and the number of iterations of cryptographic function based on the level of security needed and the hardware support. The software also allows for profiling latency for different combinations of security parameters.


## How it Works - Steps involved in CBC Encryption
- The encryption uses the [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) library to derive a master key using a secret, cipher, hashing algorithms and salt. The cipher can be one of AES128, AES256, or 2DES, and the hashing algorithm can be one of SHA256 or SHA512. 
- The master key is then used to generate an encryption key and an HMAC key. The generated cipher file is then combined with an initialization vector (IV) to create an HMAC. The created HMAC and the encryption information are packed inside the header metadata.
- For decryption, the header is extracted and unwrapped to gather information about encoding. The master key, encryption key, and the HMAC key are generated using the PBKDF2 library. The extracted HMAC is then validated, followed by the retrieval of the original file.

## Encryption and decryption Sequence
- Run the Secure file Suite implementation file(secure_file_impl.py).
- Select a file to be encrypted by clicking on "Input a file".
- Enter a password(refer to [this](https://security.harvard.edu/use-strong-passwords) to choose a good password)
- Select a Cipher type from the drop-down.
- Select a Hashing algorithm from the drop-down.
- Enter the number of iterations.
- Click the "Encrypt" button.
- The number of iterations and the corresponding latency in seconds are captured.
- A decryption window will open.
- Select a file to be decrypted by clicking on "Input a file" (file with .enc extension).
- Click the "Decrypt" button.
- A decrypted_file will be created in the same directory.

## Performance Analysis

### CPU Hardware Specification
| Processor | Intel(R) Core(TM) i5-7200U |
| :-------- | :------- |
|Microarchitecture |Kaby Lake |
|Lithography |22nm|
|Total cores |2|
|Total Threads |4| 
|Max Turbo Frequency |2.71 GHz Processor|
|Base Frequency |2.50 GHz|
|Cache |3 MB Intel® Smart Cache| 
|Bus Speed |5 GT/s|
|Thermal Design Power |15W| 
|Single Precision FLOPs/Cycle| 16 FLOPs/cycle|


### Profiling Encryption Latency for specific Hardware


| Iterations | Cipher     | Hashing Algorithm       |Latency(Seconds) |
| :-------- | :------- | :------------------------- |--------|
|10	        |AES128	|SHA256          |0.087915100040845|
|10	        |AES256	|SHA512          |0.051415799884125|
|100	    |AES128	|SHA256          |0.134783699875697|
|1,000	    |AES128	|SHA256          |0.162467800080776|          
|10,000	    |AES128	|SHA256          |0.177999000065028|
|100,000	|AES128	|SHA256          |0.260051800170913|
|1,000,000	|AES128	|SHA256          |1.59048040001653|
|1,000,000	|AES256	|SHA512          |1.12545419996604|
|1,500,000	|AES128	|SHA256          |2.28053000010550|
|2,000,000	|AES128	|SHA256          |3.12635130016133|
|5,000,000	|AES128	|SHA256          |7.17342420015484|
|10,000,000	|AES128	|SHA256          |7.69304569996893|
|10,000,000	|AES256	|SHA512          |9.66458750003948|
|10,000,000	|3DES	|SHA256          |7.92388719995506|


## Authors

- [@kishan92](https://github.com/kishan92)
- [LinkedIn](https://www.linkedin.com/in/kishan-nagendra-profile/)

