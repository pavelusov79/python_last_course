class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def __str__(self):
        return f'name: {self.name}, price: {self.price}'


class Item1(ItemDiscountReport):
    def get_info(self):
        return f'name: {self.name}'

#option 2
    @classmethod
    def get_info_parent(cls, obj):
        cls.obj = obj
        return f'name: {obj.name}'


class Item2(ItemDiscountReport):
    def get_info(self):
        return f'price: {self.price}'

#option 2
    @classmethod
    def get_info_parent(cls, obj):
        cls.obj = obj
        return f'price: {obj.price}'


i1 = Item1('banana', 50)
print(i1.get_info())
print('option 2')
p = ItemDiscount('kiwi', 80)
i1 = Item1.get_info_parent(p)
print(i1)
print('-'*15)
i2 = Item2('banana', 50)
print(i2.get_info())
print('option 2')
p = ItemDiscount('apple', 100)
i2 = Item2.get_info_parent(p)
print(i2)



