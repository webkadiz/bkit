class Unique:
    def __init__(self, items, ignore_case=False):
        copy_items = [item for item in items]

        if ignore_case:
            self.uniq_items = {item.lower(): item for item in copy_items}.values()
        else:
            self.uniq_items = set(copy_items)

    def __iter__(self):
        return (item for item in self.uniq_items)
