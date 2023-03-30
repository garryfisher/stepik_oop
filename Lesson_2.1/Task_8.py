class Point:
    @classmethod
    def __check_coords(cls, coord):
        return type(coord) in (int, float)

    def __init__(self, x, y):
        if self.__check_coords(x) and self.__check_coords(y):
            self.__x = x
            self.__y = y
        else:
            assert ValueError('int & float only')

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, *args):
        if len(args) == 4:
            self.__sp = Point(args[0], args[1])
            self.__ep = Point(args[2], args[3])
        else:
            self.__sp = args[0]
            self.__ep = args[1]

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f'Прямоугольник с координатами: '
              f'{Point.get_coords(self.__sp)} '
              f'{Point.get_coords(self.__ep)}')


rect = Rectangle(Point(0, 0), Point(20, 34))
