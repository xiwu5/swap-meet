# from .
class Vendor:
    def __init__(self, inventory=None):
        inventory = [] if inventory is None else inventory
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
    
    def get_by_id (self, id):
        for item in self.inventory:
            if item.id == id:
                return item 

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item  not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)

        return True