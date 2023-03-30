import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def select(self, a, b):
        lst = self.lst_data
        return lst[a:b + 1]

    def insert(self, data):
        lst = self.lst_data
        fields = self.FIELDS
        for x in data:
            lst.append(dict(zip(fields, tuple(x.split()))))


db = DataBase()
db.insert(lst_in)

#assert
res1 = db.select(0, 50)
lstgfghj8gh9jg2 = []
for d in lst_in:
    lstgfghj8gh9jg2.append(dict(zip(DataBase.FIELDS, d.split())))
assert res1 == lstgfghj8gh9jg2, "метод select вернул неверные данные"
res2 = db.select(0, 1)
assert res2 == lstgfghj8gh9jg2[0:2], "некорректно работает метод select"
print(True)
