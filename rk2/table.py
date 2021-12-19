class Table():
    id: int = 0

    def __init__(self):
        self.incId()
    
    @classmethod
    def getId(cls):
        return cls.id

    @classmethod
    def incId(cls):
        cls.id += 1
