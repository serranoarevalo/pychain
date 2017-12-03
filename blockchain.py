import hashlib
import json
from time import time

class Blockchain(object):
    # Blockchain class

    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self, sender, recipient, amount):
        pass

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

    @staticmethod
    def hash(block):
        # Hashes a block
        pass

    @property
    def last_block['index'] + 1(self):
        # Returns the last block of the chain
        pass
