import uuid

class Item:
    def __init__(self, id=0):
        self.id = int(uuid.uuid4())
