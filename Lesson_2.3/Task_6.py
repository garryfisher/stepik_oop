class FloatValue:
    @classmethod
    def validate(cls, obj):
        if type(obj) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, item=0.0):
        self.value = item


class TableSheet:
    def __init__(self, N, M):
        self.n = N
        self.m = M
        self.cells = [[Cell() for i in range(self.m)] for j in range(self.n)]


table = TableSheet(5, 3)
start = 1.0
for i in range(table.n):
    for j in range(table.m):
        table.cells[i][j].value = start
        start += 1.0