class StringValue:
    def __init__(self, min_length=2, max_length=50):
        self.min_ = min_length
        self.max_ = max_length

    def checking(self, value):
        return type(value) == str \
            and self.min_ <= len(value) <= self.max_

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.checking(value):
            setattr(instance, self.name, value)


class PriceValue:
    def __init__(self, max_value=10000):
        self.max_ = max_value

    def checking(self, value):
        return type(value) in (int, float) \
            and 0 <= value <= self.max_

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.checking(value):
            setattr(instance, self.name, value)


class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = list()

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price
