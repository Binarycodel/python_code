
from pyexpat import model
from turtle import Turtle
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from numpy import block

# Create your models here.


# model for creating blockchain user in the database....
class BlockchainUser(AbstractUser):
    
    Balance = models.IntegerField(null=True)
    identity = models.TextField(null=True)
    private_key = models.BinaryField()

    # @property
    # def identity(self):
    #     id = binascii.hexlify(self.public_key.export_key(format='DER')).decode('ascii')
    #     return id

class Block(models.Model):
    block_number = models.IntegerField(primary_key=True)
    transaction_count = models.IntegerField(null=True)
    nounce = models.TextField(null=True)
    previous_block_hash = models.TextField(null=True)
    block_hash = models.TextField(null=True) 

# model for creating transaction in the database...
class Transaction(models.Model):

    sender_id = models.TextField()
    receiver_id = models.TextField()
    amount_transfer = models.IntegerField()
    time_stamp = models.DateTimeField(auto_now_add=True)
    transaction_signed = models.TextField()
    block_number = models.IntegerField()
    block_number = models.ForeignKey('Block', on_delete=models.CASCADE)



