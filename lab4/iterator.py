from product import Product

class TreeIterator():
    def depthDetour(self, tree):
        for child in tree.children:
            yield child
            yield from self.depthDetour(child)