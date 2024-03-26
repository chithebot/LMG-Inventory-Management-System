import entity


class Item(entity.Entity):

    def __init__(self, name="", sku=0, category="None", quantity=0):
        entity.Entity.__init__(self, name)
        self._sku = sku
        self._category = category
        self._quantity = quantity

    @property
    def sku(self):
        return self._sku

    @sku.setter
    def sku(self, sku):
        self._sku = sku

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        self._category = category

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    def __str__(self):
        itemInfo = self.name + "\t" + str(self.sku) + "\t" + \
                   self.category + "\t" + str(self.quantity)
        return itemInfo
