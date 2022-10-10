
# from hmac import digest
from distutils.ccompiler import gen_preprocess_options
from turtle import pu
import block
from block import Block, Blocks
import client
import transaction as tr
import blockchain



akin = client.Client()
ahmed = client.Client()
bola = client.Client()
segun = client.Client()
ade = client.Client()


# creating the first transaction with genesis block...
trans0 = tr.Transaction("Genesis", akin, 500)
trans0.transaction_wrapper()

gen_block = block.GenesisBlock()
gen_block.validated_transactions.append(trans0)
hash_genesis = hash(gen_block)
gen_block.block_hash = hash_genesis
gen_block.previous_block_hash = hash_genesis



# creating a block chain 
block_chain = blockchain.Blockchain()
block_chain.add_block_to_chain(gen_block)

# block_chain.get_blocks_history(0)


def block_chaining():

    # checking the transaction pool..
    # implementing thread to modify the transaction pool by a thread at a time  
    # then update other thread.
    

    block_count = 0
    transaction_empty = False
    
    while tr.Transaction.transactions != []:
        block_count = block_count + 1
        block = Block()
        print("BLOCK  === >>>>> ", block_count)
        

        # check if blook is up to block size or transaction is still in transaction pool
        while not block.is_ready_for_mining():  
            
            # it possible not to have any tracation while validatate transaction are not
            # up to the block capacity e.g 2,3,4,5 transaction in a block
            # check transaction if remaining then if not end the transaction mining and block creation.
            if tr.Transaction.transactions == []:
                print('empty transaction pool.....')
                transaction_empty = True
                break
        
            # pool a single transacting transaction pool
            pull_transact = tr.Transaction.pull_transaction()

            # if pull_transact == None:
            #     print('pull transac')

            # if pull_transact != None :
            if pull_transact.validate_transaction() :
                # while the block size is still less than block capacity keep adding valid transaction to block....
                print('still mining transaction.............')
                block.validated_transactions.append(pull_transact)

            else:
                print('invalide transaction')        
           

        else:
            # another competition by miners for mining the block itself
            print('block mined and ready to block chain it..')
            # cheking if genesis block of subsequent block
            if len(block_chain.system) >= 2:
                last_hash_val = block_chain.system[-1].last_block_hash
            else:
                last_hash_val = block_chain.system[-1].block_hash

            #  taking the last block 
            # hash value and set it to the current block preivous hash value
            block.previous_block_hash = last_hash_val
            # setting block nounce by mining process...............................................
            block.nounce = block_chain.mine_block(block,2)
            block.block_hash = hash(block)
            # adding block to block chain
            block_chain.system.append(block)
            # if successful 
            block.last_block_hash = block.block_hash
        
        if transaction_empty:
            # another competition by miners for mining the block itself
            print('block mined and ready to block chain it..')
            # cheking if genesis block of subsequent block
            if len(block_chain.system) >= 2:
                last_hash_val = block_chain.system[-1].last_block_hash
            else:
                last_hash_val = block_chain.system[-1].block_hash

            #  taking the last block 
            # hash value and set it to the current block preivous hash value
            block.previous_block_hash = last_hash_val
            # setting block nounce by mining process...............................................
            block.nounce = block_chain.mine_block(block,2)
            block.block_hash = hash(block)
            print('Nounce type ', type(block.nounce))

            # adding block to block chain
            block_chain.system.append(block)
            # if successful 
            block.last_block_hash = block.block_hash

         
    else:
        # if no transaction in transaction pool
        print('no more transaction to mine')
        # showing all block chain data history
        print("\n========================= BLOCK HISTORY =======================")  
        block_chain.get_blocks_history(0)
        print("========================= END HISTORY =======================")  

        return 
    
# END OF BLOCK CHAINIG METHOD....... 


trans1 = tr.Transaction(akin, ahmed.identity, 150)
trans1.sign_transaction()


# trans2 = tr.Transaction(akin, ade.identity, 70)
# trans2.sign_transaction()

# trans3 = tr.Transaction(ade, akin.identity, 30)
# trans3.sign_transaction()

# trans4 = tr.Transaction(segun, bola.identity, 90)
# trans4.sign_transaction()

# trans5 = tr.Transaction(bola, ahmed.identity, 120)
# trans5.sign_transaction()



tr.Transaction.transactions.append(trans1)
# tr.Transaction.transactions.append(trans2)
# tr.Transaction.transactions.append(trans3)
# tr.Transaction.transactions.append(trans4)
# tr.Transaction.transactions.append(trans5)

# tr.Transaction.transaction_history()
# print(len(tr.Transaction.transactions))

block_chaining()