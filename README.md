

************************************************************
******************* CBC Encryption Suite *******************
************************************************************
Securing Files using CBC Encryption
 This security Software application is used to encrypt/decrypt a file by allowing the user to chose a secret, cipher type(AES/DES), hashing algorithm(SHA256/SHA512) and the number of iterations of cryptographic function based on the level of security needed and the hardware support. The software also allows to profile latency for different combinations.



*********ENCRYPTION & DECRYPTION SEQUENCE*********
-> Run the Secure file Suite implementation file(secure_file_impl.py)
-> Select a file to be encrypted by clicking on "Input a file"
-> Enter password(refer to https://www.kryptel.com/articles/encryption_passwords.php to choose a good password)
-> Select Cipher type from dropdown
-> Select Hashing algorithm from dropdown
-> Enter the number of iterations
-> click the "Encrypt" button
-> the number of iterations and corresponding latency in seconds is shown
-> A decryption window is opens
-> Select a file to be decrypted by clicking on "Input a file"(file with .enc extension)
-> Click the "Decrypt" button
-> a decrypted_file is created on the same directory


*******Command to Run*******
python secure_file_suite_impl.py



****PERFORMANCE ANALYSIS****
CPU Specifications


Profiling latency for the above hardware by selecting few relavant combinations:

Profiling the Encryption time for few relavent combinations:
************************************************************
Iterations |Cipher |Hashing        |Latency(seconds)
************************************************************
10	        AES128	SHA256          0.087915100040845
10	        AES256	SHA512          0.051415799884125

100	        AES128	SHA256          0.134783699875697
1,000	    AES128	SHA256          0.162467800080776          
10,000	    AES128	SHA256          0.177999000065028
100,000	    AES128	SHA256          0.260051800170913

1,000,000	AES128	SHA256          1.59048040001653
1,000,000	AES256	SHA512          1.125454199966043

1,500,000	AES128	SHA256          2.2805300001055
2,000,000	AES128	SHA256          3.12635130016133
5,000,000	AES128	SHA256          7.17342420015484

10,000,000	AES128	SHA256          7.69304569996893
10,000,000	AES256	SHA512          9.66458750003948
10,000,000	3DES	SHA256          7.92388719995506

