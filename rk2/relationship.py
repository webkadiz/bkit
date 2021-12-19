from table import Table

class Link:
    ONE_TO_MANY: int = 1
    MANY_TO_ONE: int = 2
    MANY_TO_MANY: int = 3


class Relationship:
    def __init__(self, tableFirst: Table, tableSecond: Table, relation, fk=''):
        self.tableFirst = tableFirst
        self.tableSecond = tableSecond
        self.relation = relation
        self.fk = fk
        self.many_to_many = []
    
    def link(self, objectFirst, objectSecond):
        if self.relation == Link.ONE_TO_MANY:
            assert self.fk, 'Set foreign key'
            setattr(objectSecond, self.fk, objectFirst.id)

        elif self.relation == Link.MANY_TO_MANY:
            self.many_to_many.append([objectFirst.id, objectSecond.id])
    
    def iter(self, tableFirst, tableSecond):
        result = []

        if self.relation == Link.ONE_TO_MANY:
            for recordFirst in tableFirst:
                for recordSecond in tableSecond:
                    if getattr(recordSecond, self.fk) == recordFirst.id:
                        result.append([recordFirst, recordSecond])

        elif self.relation == Link.MANY_TO_MANY:
            for idFirst, idSecond in self.many_to_many:
                for recordFirst in tableFirst:
                    for recordSecond in tableSecond:
                        if idFirst == recordFirst.id and idSecond == recordSecond.id:
                            result.append([recordFirst, recordSecond])

        return result
