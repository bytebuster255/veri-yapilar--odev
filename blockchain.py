import hashlib

class Block:
    def __init__(self, data):
        self.data = data
        self.previous_hash = "0"
        self.hash = ""
        self.previous = None

    def calculate_hash(self):
        text = str(self.data) + str(self.previous_hash)
        return hashlib.sha256(text.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_block(self, data):
        new_block = Block(data)
        if self.head is None:
            new_block.previous_hash = "0"
            new_block.previous = None
            new_block.hash = new_block.calculate_hash()
            self.head = new_block
            self.tail = new_block
        else:
            new_block.previous_hash = self.tail.hash
            new_block.previous = self.tail
            new_block.hash = new_block.calculate_hash()
            self.tail = new_block

    def display_chain(self):
        temp = self.tail
        while temp is not None:
            print(f"Block -> Data: {temp.data}, Hash: {temp.hash}, Previous Hash: {temp.previous_hash}")
            temp = temp.previous

    def verify_chain(self):
        temp = self.tail
        valid = True

        while temp is not None:
            if temp.hash != temp.calculate_hash():
                valid = False
                break

            if temp.previous is not None:
                if temp.previous_hash != temp.previous.hash:
                    valid = False
                    break
            else:
                if temp.previous_hash != "0":
                    valid = False
                    break

            temp = temp.previous

        if valid:
            print("\nBlockchain is valid.")
        else:
            print("\nBlockchain is invalid.")

chain = Blockchain()
chain.add_block("First block")
chain.add_block("Second block")
chain.add_block("Third block")

chain.display_chain()
chain.verify_chain()