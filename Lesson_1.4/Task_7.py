import sys


# здесь объявляется класс StreamData
class StreamData:
    def create(self, fields, lst_values):
        len_f = len(fields)
        len_v = len(lst_values)
        if len_f == len_v:
            for x in range(len_f):
                setattr(self, fields[x], lst_values[x])
        return len_f == len_v


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
