
from http.client import HTTPResponse
from multiprocessing.connection import Client
import re
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from numpy import block
from requests import RequestException
from . models import Block, BlockchainUser, Transaction
from django.contrib.auth.models import auth, User
from django.conf import settings
from . import client
from . import transaction as tr
from . import blockchain as bchain

# Create your views here.

def index(request):

    transaction = list(Transaction.objects.all())
    print([t.amount_transfer for t in transaction])
    return render(request, 'index.html', {"transactions":transaction})


def login(request):

    if request.method == "POST":

        email = request.POST['email']
        password =  request.POST['password']
        print(f'email {email} password {password}')

        user = auth.authenticate(username=email , password=password)

        if user is not None :
            auth.login(request, user)
            return redirect('/')
        else:
            print('login failed')
            return redirect('login')
    else:

        return render(request, 'login.html')




def register(request):

    if request.method == "POST":
      
        fname = request.POST['fname']
        lname = request.POST['lname']
        # username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        # print(f'{fname} {lname} {email} {password} {cpassword}')

        if fname != '' and lname != ''  and email != '' and password != '' :

            if password == cpassword:
                cl = client.Client()
                identity = cl.identity
                balance = cl.balance
                pr_key = cl.private_key.export_key(format='DER')

                bc_user = BlockchainUser.objects.create_user(username=email, password=password, first_name=fname, last_name=lname, email=email, identity=identity, Balance=balance, private_key= pr_key)
                bc_user.save()
                # (username=username, password=password, first_name=fname, last_name=lname, email=email, identity=identity, Balance=balance)
                # bc_user.save()

                return redirect('/login')
            else: 
                # else for password checking 
                print('Password Not Matching')

        else: 
            # for checking if user enter valid data
            print('Plean Enter valid data')
            return redirect('/register')
    else:
        return render(request, 'register.html')

def account(request):
    if BlockchainUser.is_authenticated:
        print('user is authenticated')
        return render(request, 'account.html')
    else:
        print('user not authenticated')
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')



def transaction(request):
    if BlockchainUser.is_authenticated:
        
        # perform transaction if only user is authenticated..
        value = request.POST['amount']
        address = request.POST['address']

        # checking for sufficient balance and negative balance
        print(f'Value {value} : address {address}')
        current_user = request.user
        dataset = BlockchainUser.objects.filter(identity=address.strip())
        
        print('Current user balance', len(dataset))
        print('value :', value)
        # current_user.identity = "Genesis"
        # current_user.first_name = "Genesis"
        # current_user.Balance = 500
        # cl = client.Client()
        # current_user.private_key = cl.private_key.export_key(format='DER')
        # current_user.save()

        # checking if user exist
        if len(dataset) != 0:
            recipient = dataset[0]
            # checking if retrieved user balance 
            if int(value) < (current_user.Balance-10) :
                
                
                # transaction helper class
                transact =  tr.Transaction(current_user, recipient.identity, value)
                
                # getting the last block number
                bl = Block.objects.all().last()
                print('BLOCK NUMBER : ', bl.block_number)

                # creating a transaction instance..... for genesis block
                if current_user.identity == "Genesis":
                    print("USER IS GENESIS")

                    # A CONDITION HAVE TO MEET BEFORE CREATING A BLOCK... 
                    if len(Transaction.objects.filter(block_number_id=bl.block_number)) % 2 == 0  :
                        
                        print('new block can now be created : ', (len(Transaction.objects.all())) )
                        # last block update nouce and block hash data ... minin process... check if its genesis...
                        if bl.block_number >= 0 :
         
                            Block.objects.create(block_number=(bl.block_number+1) , transaction_count = len(Transaction.objects.filter(block_number_id=bl.block_number)), nounce=0, previous_block_hash=bl.block_hash, block_hash="")
                            print(' OTHER BLOCK CREATED BY GENESIS ....')

                            sub_block = Block.objects.filter(block_number=(bl.block_number+1)).first()
                            bc_chain = bchain.Blockchain()
                            sub_block.nounce =  bc_chain.mine_block(sub_block, 1)
    
                                # creating intance blovk
                            # block_instance = Block()
                            # block_instance.block_number = sub_block.block_number
                            # block_instance.transaction_count = sub_block.transaction_count
                            # block_instance.nounce = sub_block.nounce
                
                            # sub_block.previous_block_hash = bl.previous_block_hash
                            sub_block.block_hash = hash(str(sub_block))
                            print("HASH VALUE SUB BLOCK: ", hash(str(sub_block)))
                            sub_block.save()

                        if bl==None:
                            print('GENESIS FOR THE FIRST TIME') 
                            Block.objects.create(block_number=0 , transaction_count=1, nounce=0, previous_block_hash="", block_hash="")
                            print(' GENESIS BLOCK CREATED....')
                            
                            # updating gen block information
                            gen_block = Block.objects.filter(block_number=0)
                            bc_chain = bchain.Blockchain()
                            gen_block.nounce =  bc_chain.mine_block(gen_block, 1)
                            gen_block.previous_block_hash = hash(gen_block)
                            gen_block.block_hash = hash(gen_block)
                            gen_block.save()
                        


                    print('keep uploading transaction') 
                    # Block.objects.create(block_number=bl.block_number , transaction_count=len(Transaction.objects.filter(block_number_id=bl.block_number)), nounce=0, previous_block_hash="", block_hash="")
                    # print('BLOCK CREATED....')


                    # getting last block number  before updating transaction
                    last_block = Block.objects.all().last()
                    print('BLOCK NUMBER : ', last_block.block_number)

                    # CREATING TRANSACTION... TRANSACTION SHOULD STILL TAKE PLACE 
                    Transaction.objects.create(sender_id=transact.get_sender_id(), receiver_id=transact.get_reciepient_id(), 
                    amount_transfer=transact.get_value(), transaction_signed=transact.sign_transaction(), block_number_id=last_block.block_number)
                    
                    # update current user balance and reciepient .......
                    balance = current_user.Balance
                    new_balance = balance - int(value)
                    current_user.Balance = new_balance
                    current_user.save()
                    recipient.Balance = recipient.Balance + int(value)
                    recipient.save()

                    print('transaction successful')                   
                else:
                    # for non genesis block........
                    # CREATE NEW BLOCK ONLY IF THIS CONDITION I MET
                    if len(Transaction.objects.filter(block_number_id=bl.block_number)) % 2 == 0  :
                       
                        Block.objects.create(block_number=(bl.block_number+1) , transaction_count = len(Transaction.objects.filter(block_number_id=bl.block_number)), nounce=0, previous_block_hash=bl.block_hash, block_hash="")
                        print(' OTHER BLOCK CREATED BY USER ....')
                        sub_block = Block.objects.filter(block_number=(bl.block_number+1))
                        bc_chain = bchain.Blockchain()
                        sub_block.nounce =  bc_chain.mine_block(sub_block, 1)
                        sub_block.previous_block_hash = bl.previous_block_hash
                        sub_block.block_hash = hash(sub_block)
                        sub_block.save()

# ====================================== ============================================================

                    # getting last block number  before updating transaction
                    last_block = Block.objects.all().last()
                    print('BLOCK NUMBER : ', last_block.block_number)

                    Transaction.objects.create(sender_id=transact.get_sender_id(), receiver_id=transact.get_reciepient_id(), 
                    amount_transfer=transact.get_value(), transaction_signed=transact.sign_transaction(), block_number_id=last_block.block_number)
                    # update current user balance and reciepient .......
                    balance = current_user.Balance
                    new_balance = balance - int(value)
                    current_user.Balance = new_balance
                    current_user.save()

                    recipient.Balance = recipient.Balance + int(value)
                    recipient.save()
                    print('transaction completed... ')
            else:
                print('invalid balance')
        else:
            print("Invalid Identity")

       
        # BlockchainUser.objects.filter


        # print('transaction called')
    return render(request, 'account.html')