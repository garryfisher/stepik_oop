class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        setattr(self, 'data', data)

    def draw(self, lst):
        limit = self.LIMIT_Y
        res = ''
        for x in lst:
            if x in range(limit[0], limit[1] + 1):
                res += f'{x} '
        print(res.strip())


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw(getattr(graph_1, 'data'))
