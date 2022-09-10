import binascii
import enchant
import Crypto
import Crypto.Random as rand
from Crypto.PublicKey import RSA


class Client:
    pass

    def __init__(self) -> None:
        random_val = rand.new().read
        # generating private, and public key
        self.private_key = RSA.generate(1024, random_val)
        self.public_key = self.private_key.publickey()
        #print(self.public_key)

        self.identity:None
        self.balance = 0

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
