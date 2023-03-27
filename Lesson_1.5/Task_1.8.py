class Cart:
    def __init__(self):
        self.goods = list()

    def add(self, *gd):
        for x in gd:
            self.goods.append(x)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f"{g.name}:{g.price}" for g in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
tv1 = TV('Sony', 350)
tv2 = TV('LG', 320)
table1 = Table('ikea', 100)
notebook1 = Notebook('Aser', 400)
notebook2 = Notebook('Huawei', 430)
cup1 = Cup('Drink Cup', 10)
cart.add(tv1, tv2, table1, notebook1, notebook2, cup1)