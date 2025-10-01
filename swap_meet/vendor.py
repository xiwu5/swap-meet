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
        
        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)

        return True
    
    def swap_first_item(self, other_vendor):
        if not other_vendor.inventory or not self.inventory:
            return False 
        
        my_first_item = self.inventory[0]
        other_first_item = other_vendor.inventory[0]
        self.swap_items(other_vendor, my_first_item, other_first_item)

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
                best_item = item
        return best_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        item_other_vendor_wants_to_receive = self.get_best_by_category(their_priority)
        item_vendor_wants_to_receive = other_vendor.get_best_by_category(my_priority)

        if item_other_vendor_wants_to_receive is None or item_vendor_wants_to_receive is None:
            return False
        
        self.swap_items(other_vendor, item_other_vendor_wants_to_receive, item_vendor_wants_to_receive)
        
        return True
        