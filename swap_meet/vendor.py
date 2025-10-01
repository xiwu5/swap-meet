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
        return False
    
    def get_by_id (self, id):
        for item in self.inventory:
            if item.id == id:
                return item 

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item  not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)
        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)

        return True
    
    def swap_first_item(self, other_vendor):
        if not other_vendor.inventory or not self.inventory:
            return False 
        
        my_first_item = self.inventory[0]
        other_vendor.inventory.append(my_first_item)
        self.inventory.remove(my_first_item)
        self.inventory.append(other_vendor.inventory[0])
        other_vendor.inventory.remove(other_vendor.inventory[0])

        return True
    
    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.get_category() is category:
                items.append(item)
        return items
    
    def get_best_by_category(self, category):
        matched_category = self.get_by_category(category)

        if not matched_category:
            return None
        
        highest_condition = -1
        for item in matched_category:
            if item.condition > highest_condition:
                highest_condition = item.condition
            return item