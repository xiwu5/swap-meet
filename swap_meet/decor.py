import uuid
class Decor:
    def __init__(self, id=None, width=None, length=None):
        self.id = int(uuid.uuid4()) if id is None else id
        self.width = 0 if width is None else width
        self.length = 0 if length is None else length
    
    def get_category(self):
        return 'Decor'
    
    def __str__(self):
        return f"An object of type Decor with id {self.id}. "f"It takes up a {self.width} by {self.length} sized space."
