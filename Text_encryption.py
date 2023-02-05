
from cryptography.fernet import Fernet

def key_gen():
 key = Fernet.generate_key()
 print("The key generated: {}".format(key))
 with open("pass.key", "wb") as key_file: key_file.write(key)
key_gen()
def call_key():
     return open("pass.key", "rb").read()

key = call_key()
slogan = input("Enter the text to be encrypted:").encode()
 
a = Fernet(key)
coded_slogan = a.encrypt(slogan)
print("The encrypted text is {}".format(coded_slogan))

key = call_key()
b = Fernet(key)
decoded_slogan = b.decrypt(coded_slogan)
print("The decrypted text is {}".format(decoded_slogan))
