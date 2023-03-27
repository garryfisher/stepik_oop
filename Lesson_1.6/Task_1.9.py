# здесь объявляется класс Point
class Point:
    def __new__(cls, *args, **kwargs):
        cls.x, cls.y = args
        cls._copy = super().__new__(cls)

        return cls._copy

    def clone(self):
        return Point(self.x, self.y)


pt = Point(4, 5)
pt_clone = pt.clone()
