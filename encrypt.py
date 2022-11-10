import base64
from cryptography.fernet import Fernet
from datetime import datetime
import time

#Input the name of the file to be encrypted

file_name = input("Enter file name along with extension: ")

#Convert the input file to Base 64 string

with open(file_name, "rb") as img_str:
    b64Str = base64.b64encode(img_str.read())
#print(b64Str)


# Prepearing the key

key = Fernet.generate_key()

# Writting the key into key.file

with open ('key.file', 'wb') as file:  
    file.write(key)  

#Current timestamp

ts = time.time()
# print(ts)

# Using the key to encrypt the string using fernet

f = Fernet(key)
encryption = f.encrypt(b64Str)
x=f.extract_timestamp(encryption)

# Time taken for running

print("Time taken to run:",ts-x)


# Writing the encrypted file in encryption.file

with open('encryption.file', "wb") as file:
  file.write(encryption)

