import os
from getpass import getpass as GP
from Crypto.Cipher import AES
from Crypto import Random


#Prompts password, the default prompt if not specified is Password:
#When use in terminal, password entered by user will not be echoed.
password = GP(prompt="password:", stream=None)
print(password)

#use os.urandom() method to create a random 16 bytes string
#convert to bytes. On this example I want to use AES-128 hence 16bytes key.
#16, 24, 32bytes are AES-128,192 and 256 bits respectively.
key = bytes(os.urandom(16))

print(key)

#To generate an initializing vector, fixed block size is 16 bytes.
iv = Random.new().read(AES.block_size)
print(iv)


#Create a cipher to use for encryption
cipher = AES.new(key, AES.MODE_CFB, iv)
print(cipher)#object

#encrypts the password entered by user
cipherText = cipher.encrypt(password)
print(cipherText)

#ciphertext is in bytes, so i open create a file - password.enc
#write the bytes into this file
with open('password.enc', 'wb') as f:
    f.write(cipherText)

#Create a decipher to decrypt the ciphertext
decipher = AES.new(key, AES.MODE_CFB, iv)
print(decipher)

#read byte from file
with open ('password.enc', 'rb') as f:
    ctext = f.read()

#decrypt the ciphertext
encoded_Text = decipher.decrypt(ctext)
print(encoded_Text)


#To convert the plaintext in bytes to string, use decode "utf-8"
plain_text = encoded_Text.decode('utf-8')
print(plain_text)
