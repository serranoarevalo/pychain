import hashlib
import json
from time import time
from uuid import uuid4

from flask import Flase

class Blockchain(object):
    # Blockchain class

    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(proof=100, previous_hash=1)

    def new_block(self, proof, previous_hash=None):
        
        """
        Creates a new block in the blockchain
        
        :param proof: <init> The proof given by the Proof of Work algorithm
        :param previous_hash: (optional) <str> Hash of the previos block
        :return: <dict> New block
        
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        self.current_transactions = []

        self.chain.append(block)

        return block

    def new_transaction(self):
        
        """
        Creates a new transaction to go into the next mined Block

        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <str> Amount
        :return: <init> The index of the Block that will hold this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        return self.last_block['index'] + 1

    def proof_of_work(self, last_proof):
        """
        Simple Proof of Work Algorithm:

        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
         - p is the previous proof, and p' is the new proof
        :param last_proof: <int>
        :return: <int>
        """

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?

        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        """

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    @staticmethod
    def hash(block):

        """
        Creates a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
        """

        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        # Returns the last block of the chain
        return self.chain[-1]


app =  Flask(__name__)

node_identifier = str(uuid4()).replace('-', '')

blockchain = Blockchain()


@app.route('/mine', methods=["GET"])
def mine():
    return "We will mine a new block"

@app.route('/transactions/new', methods=["POST"])
def new_transaction():
    # Get the POST'ed values
    values = request.get_json()



    # Check that all the required fields are in the POST'ed data
    required = ['sender', 'recipient', 'amount']
    if not all(field in values for field in required)
        return "Missing values", 400

    # Create a new transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = { 'message': f'Transaction will be added to Block {index}'}
    
    return jsonify(response), 201

@app.route('/chain', methods=["GET"])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
