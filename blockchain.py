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