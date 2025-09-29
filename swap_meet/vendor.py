class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory
    
    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item
    
    def remove(self, new_item):
        if new_item in self.inventory:
            self.inventory.remove(new_item)
            return new_item
        else: 
            return False
