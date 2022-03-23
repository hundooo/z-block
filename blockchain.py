class BlockChain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
    
    @staticmethod
    def hash(block):
        pass

    def new_block(self):
        pass

    @property
    def last_block(self):
        return self.chain[-1]

    def new_transactions(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1