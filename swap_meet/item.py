import uuid

class Item:
    def __init__(self, id=None, condition=0):
        self.id = int(uuid.uuid4()) if id is None else id
        self.condition = condition

    def get_category(self):
        return "Item"
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        if self.condition == 5:
            return "Mint"
        elif self.condition == 4:
            return "Slightly used"
        elif self.condition == 3:
            return "Good"
        elif self.condition == 2:
            return "Heavily used"
        elif self.condition == 1:
            return "You probably want a glove for this one..."
        else:
            return "Broken"
