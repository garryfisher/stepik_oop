# здесь объявляются все необходимые классы
class Graph:
    def __init__(self, data, is_show=True):
        self.data = data[:]

        self.is_show = is_show

    def set_data(self, data):
        self.data = data

    def show_table(self):
        if self.is_show:
            print(*self.data)
        else:
            print('Отображение данных закрыто')

    def show_graph(self):
        if self.is_show:
            print('Графическое отображение данных:', *self.data)
        else:
            print('Отображение данных закрыто')

    def show_bar(self):
        if self.is_show:
            print('Столбчатая диаграмма:', *self.data)
        else:
            print('Отображение данных закрыто')

    def set_show(self, fl_show=True):
        if not fl_show:
            self.is_show = False


# считывание списка из входного потока (эту строку не менять)
data_graph = list(map(int, input().split()))

# здесь создаются объекты классов и вызываются нужные методы
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(fl_show=False)
gr.show_table()

#assert
assert isinstance(gr, Graph) and hasattr(Graph, 'set_data') and hasattr(Graph, 'show_table') and hasattr(Graph, 'show_graph') and hasattr(Graph, 'show_bar') and hasattr(Graph, 'set_show')

assert gr.data == data_graph, "данные в объекте класса Graph и в списке data_graph отличаются"
assert hasattr(gr, 'is_show'), "объект gr не имеет атрибута is_show"

data = [1, 2, 3, 4]
gr2 = Graph(data)
gr3 = Graph(data)
gr3.data.append(5)

assert gr2.data != gr3.data, "локальный атрибут data должен быть уникальным (своим собственным) в каждом объекте класса Graph"