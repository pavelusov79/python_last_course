class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def new_price(self):
        if self.price < 100:
            return self.price + 20
        else:
            return self.price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        if self.price < 100:
            return f'name: {self.name}, price: {ItemDiscount.new_price(self)}'
        else:
            return f"name: {self.name}, price: {self.price}"


goods = ItemDiscountReport('apple', 90)
print(goods.get_parent_data())
print(f'new price called from child class: {goods.new_price()}')
print('-'*40)
p = ItemDiscount('banana', 50)
print(f'price called from parent class: {p.price}')
print(f'new price called from parent class: {p.new_price()}')

