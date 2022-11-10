import base64
from cryptography.fernet import Fernet
from datetime import datetime
import time

# opening the encrypted file
with open('encryption.file', 'rb') as encryption_file:
    encryption = encryption_file.read()


#Reading the Key used during Encryption

with open("key.file", "rb") as key_file:
    key = key_file.read()
    print(key)

#Current timestamp

ts = time.time()
# print(ts)

#Decrypting the encrypted file
f= Fernet(key)
decryption=f.decrypt(encryption)

x=time.time()

#Printing the decrpted file into its orginal state

file_name = input("Enter orginal file name along with extension used during encryption: ")


with open('new_'+file_name, 'wb') as decryption_file:
    decryption_file.write(base64.b64decode(decryption))
    decryption_file.close()

print("Time taken to run",x-ts)