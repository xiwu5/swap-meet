from swap_meet.item import Item
class Decor(Item):
    def __init__(self, id=None, condition=0, width=None, length=None):
        super().__init__(id, condition)
        self.width = 0 if width is None else width
        self.length = 0 if length is None else length
    
    def get_category(self):
        return 'Decor'
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}. "f"It takes up a {self.width} by {self.length} sized space."
