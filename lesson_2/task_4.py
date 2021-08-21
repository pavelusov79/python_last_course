class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, discount):
        self.discount = discount
        super().__init__(name, price)

    def discount_price(self):
        return round(self.price - self.price * self.discount / 100)

    def __str__(self):
        return f"name: {self.name}, price: {self.price}, discount_price: {self.discount_price()}"


goods = ItemDiscountReport('apple', 90, 20)
print(goods)


