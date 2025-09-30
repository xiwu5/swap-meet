import uuid

class Clothing:
    def __init__(self, id=None, fabric="Unknown"):
        self.id = int(uuid.uuid4()) if id is None else id
        self.fabric = fabric if fabric is "Unknown" else fabric

    def get_category(self):
        return "Clothing"
    
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."