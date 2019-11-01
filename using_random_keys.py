import cryptography
from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)
#b'6MDtNAPEoWiO7ie_uIFOUiGvXwECjQ84AMukC1AYPzE='

#encoding the message by converting it into bytes
message = "password or message".encode()

#we've printed one random key and to be able to use it as a key
key = b'6MDtNAPEoWiO7ie_uIFOUiGvXwECjQ84AMukC1AYPzE='

f = Fernet(key)
encrypted = f.encrypt(message)
print(encrypted)



#to decrypt any encrypted message we use Fernet(key).decrypt(encrypted)
decrypted = f.decrypt(encrypted)
print(decrypted)


#decode the byte message
message = decrypted.decode("utf8")
print(message)
