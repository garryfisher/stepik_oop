# Из входного потока читаются строки данных с помощью команды:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
# в формате: id, name, old, salary (записанные через пробел). Например:
#
# 1 Сергей 35 120000
# 2 Федор 23 12000
# 3 Иван 13 1200
# ...
#
# То есть, каждая строка - это элемент списка lst_in.
#
# Необходимо в класс DataBase:
#
# class DataBase:
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')
# добавить два метода:
#
# select(self, a, b) - возвращает список из элементов списка lst_data в диапазоне [a; b] (включительно) по их индексам (не id, а индексам списка); также учесть, что граница b может превышать длину списка.
# insert(self, data) - для добавления в список lst_data новых данных из переданного списка строк data;
#
# Каждая запись в списке lst_data должна быть представлена словарем в формате:
#
# {'id': 'номер', 'name': 'имя', 'old': 'возраст', 'salary': 'зарплата'}
#
# Например:
#
# {'id': '1', 'name': 'Сергей', 'old': '35', 'salary': '120000'}
#
# Примечание: в этой задаче число элементов в строке (разделенных пробелом) всегда совпадает с числом полей в коллекции FIELDS.
#
# P. S. Ваша задача только добавить два метода в класс DataBase.
#
# Sample Input:
#
# 1 Сергей 35 120000
# 2 Федор 23 12000
# 3 Иван 13 1200


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
