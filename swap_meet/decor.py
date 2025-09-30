import uuid
class Decor:
    def __init__(self, id=None):
        self.id = int(uuid.uuid4()) if id is None else id
    
    def get_category(self):
        return 'Decor'
    
    def __str__(self):
       return f"An object of type Decor with id {self.id}. " "It takes up a 0 by 0 sized space."
