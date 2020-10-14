import cryptography
from cryptography.fernet import Fernet as fer
key = fer.generate_key()
f=fer(key)

print('------Type the message-----')
msg = input().encode()
print("***message recorded***")
print("Type the password to encrypt the message")
p1 = input()
token = f.encrypt(msg)

print ("Password please to decrypt the message : ")
p2 = input()
if(p1 == p2):
    print("Here is your decrypted message")
    print(f.decrypt(token))
    
    

    
