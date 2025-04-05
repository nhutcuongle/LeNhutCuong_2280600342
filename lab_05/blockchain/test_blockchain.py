from blockchain import Blockchain

# Testing the blockchain
my_blockchain = Blockchain()

num_tx = int(input("Nhập số lượng: "))
for i in range(num_tx):
    sender = input(f"Nhập tên giao dịch {i+1}: ")
    receiver = input(f"Nhập tên nhận {i+1}: ")
    amount = float(input(f"Nhập số tiền {i+1}: "))
    my_blockchain.add_transaction(sender, receiver, amount)

# Mining a new block
previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof
new_proof = my_blockchain.proof_of_work(previous_proof)
previous_hash = previous_block.hash

my_blockchain.add_transaction('Genesis', 'Miner', 1)
new_block = my_blockchain.create_block(new_proof, previous_hash)

# Displaying the blockchain
for block in my_blockchain.chain:
    print(f"Block #{block.index}")
    print("Timestamp:", block.timestamp)
    print("Transactions:", block.transactions)
    print("Proof:", block.proof)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print("------------------------------")

# Check if the blockchain is valid
print("Is Blockchain Valid:", my_blockchain.is_chain_valid(my_blockchain.chain))
