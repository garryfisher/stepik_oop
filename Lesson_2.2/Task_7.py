class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = x if self.is_validate(x) else 0
        self.__y = y if self.is_validate(y) else 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if self.is_validate(x):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if self.is_validate(y):
            self.__y = y

    @classmethod
    def is_validate(cls, num):
        return isinstance(num, (int, float))\
            and cls.MIN_COORD <= num <= cls.MAX_COORD

    @staticmethod
    def norm2(vector):
        return vector.x ** 2 + vector.y ** 2
