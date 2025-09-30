import uuid

class Item:
    def __init__(self, id=None, condition=None):
        self.id = int(uuid.uuid4()) if id is None else id
        self.condition = 0.0 if condition is None else condition

    def get_category(self):
        return "Item"
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description():
        pass
