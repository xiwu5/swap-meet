import uuid

class Electronics:
    def __init__(self, id=None, type="Unknown"):
        self.id = int(uuid.uuid4()) if id is None else id
        self.type = type if type is "Unknown" else type
        
    def get_category(self):
        return "Electronics"

    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."