import uuid

class Electronics:
    def __init__(self, id=None):
        self.id = int(uuid.uuid4()) if id is None else id
        
    def get_category(self):
        return "Electronics"