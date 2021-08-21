class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f"name: {self.name}, price: {self.price}"


goods = ItemDiscountReport('apple', 100)
print(goods.get_parent_data())
