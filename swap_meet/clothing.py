from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, condition=0, fabric="Unknown"):
        super().__init__(id, condition)
        self.fabric = fabric if fabric is "Unknown" else fabric

    def get_category(self):
        return "Clothing"
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}. It is made from {self.fabric} fabric."