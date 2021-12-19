from table import Table

class Music(Table):
    """Музыкальное произведение"""
    def __init__(self, name):
        super().__init__()
        self.id = self.getId()
        self.name = name
    
    def __iter__(self):
        return iter((self.name,))
