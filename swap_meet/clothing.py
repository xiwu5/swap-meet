import uuid

class Clothing:
    def __init__(self, id=None):
        self.id = int(uuid.uuid4()) if id is None else id