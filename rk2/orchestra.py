from table import Table

class Orchestra(Table):
    """Оркестр"""
    fk_music = 'music_id'

    def __init__(self, name, amount):
        super().__init__()
        self.id = self.getId()
        self.name = name
        self.amount = amount
        self.music_id = 0

    def __iter__(self):
        return iter((self.name, self.amount))
