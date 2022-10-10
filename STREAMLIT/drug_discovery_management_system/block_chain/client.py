import binascii
from random import random
import Crypto
import Crypto.Random as rand
from Crypto.PublicKey import RSA



class Client:

    def __init__(self) -> None:
        random_val = rand.new().read
        # generating private, and public key
        self.private_key = RSA.generate(1024, random_val)
        self.public_key = self.private_key.publickey()
        # self.signer = PRCS1_V1_5.new(self.private_key)
        #print(self.public_key)

        self.identity : None

        # OTHER USE ATTRIBUTE 

    @property
    def identity(self):
        id = binascii.hexlify(self.public_key.export_key(format='DER')).decode('ascii')
        return id

    @identity.setter
    def identity(self):
        pass 


    def __str__(self) -> str:
        string = f'identity ->> {self.identity}'
        return string


def byte_to_string(binary_data):
    string = binary_data.decode('utf8')
    return string

def string_to_byte(string_data):
    byte = string_data.encode('utf-8')
    return byte







client = Client()


print(client.private_key)
print("=======================================================")
key = client.private_key.export_key(format='DER')
print(type(key))

im_key = RSA.import_key(key)
print(im_key)