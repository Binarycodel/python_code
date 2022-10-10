# transaction python script file 
import datetime as dt
import collections
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
import binascii
import user as us
from Crypto.Hash import SHA256

class Messages:

    # need a logic to restric one minner to pop at a time
    messages = []
   
    def __init__(self, sender_object, recipient, message) -> None:
        
        self.sender_object = sender_object
        self.recipient = recipient
        self.message = message
        self.time_stamp = dt.datetime.now()
        self.validated = False
    

    def transaction_wrapper(self):
        
        if self.sender_object == 'Genesis':
            identity = 'Genesis'
        else:
            identity = self.sender_object.identity
        
        diction = collections.OrderedDict({
            'sender': identity,
            'recipient': self.recipient,
            'message':self.message,
            'time':self.time_stamp
        })

        return diction 

    @classmethod
    def pull_transaction(cls):
        if len(cls.messages) != 0:
            return cls.messages.pop()
        else :
            print('no current transaction....')
            return None
    

    def sign_transaction(self):

        private_key = self.sender_object.private_k
        digital_signature = PKCS1_v1_5.new(private_key)
        print('signature' , digital_signature)
        hash = SHA.new(str(self.transaction_wrapper()).encode('utf8'))
        hex_val = binascii.hexlify(digital_signature.sign(hash)).decode('ascii')
        return hex_val 

    
    def validate_transaction(self):

        # checking balance of client...
        # checking for valid sender and reciepient account..
        # checking valid amount been sent....
        return True

  
    def transaction_data(self):
        
        dict = self.transaction_wrapper() 
        print ("SENDER======> : " + str(dict['sender'])) 
        print ('-----') 
        print ("RECIPIENT==> : " + str(dict['recipient'])) 
        print ('-----') 
        print ("VALUE======> : " + str(dict['value'])) 
        print ('-----') 
        print ("TIME=======> : " + str(dict['time'])) 
        print ('-----')

    
    @classmethod
    def transaction_history(self, start=0):
        for transaction in Transaction.transactions[start:]:
            transaction.transaction_data()
            print('--------- END -----------')


    @classmethod
    def transaction_history_range(self, start=0, stop=3):
        for transaction in Transaction.transactions[start:]:
            transaction.transaction_data()
            print('--------- END -----------')



# ================================================================================

# sender = us.User()
# reciver = us.User()

# # value validation could be done by reconding another transaction and 
# # perform the digital_signature comparison....
# tran = Messages(sender, reciver.identity , 'this is cool message')
# t1 = tran.sign_transaction()



# tran.message = "this is cool message"
# t2 = tran.sign_transaction()

# print(t1==t2)

