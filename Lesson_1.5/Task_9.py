import sys


# здесь объявляются все необходимые классы
class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


# считывание списка из входного потока (эту строку не менять)
lst_in = list(map(str.strip, sys.stdin.readlines())) # список lst_in в программе не менять

# здесь создаются объекты классов и вызываются нужные методы
head_obj = ListObject(lst_in[0])
start_obj = head_obj
for string in range(1, len(lst_in)):
    new_obj = ListObject(lst_in[string])
    start_obj.link(new_obj)
    start_obj = new_obj

#assert
assert isinstance(head_obj, ListObject) and hasattr(ListObject, 'link')

lst_data = []
h = head_obj
while h:
    lst_data.append(h.data)
    h = h.next_obj

assert lst_in == lst_data, "данные в объектах ListObject не совпадают с прочитанными данными (списком lst_in)"