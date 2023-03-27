# здесь объявите класс TriangleChecker
class TriangleChecker:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        a = self.a
        b = self.b
        c = self.c
        for x in [a, b, c]:
            if type(x) not in (int, float) or x < 0:
                return 1
        if a + b < c or a + c < b or b + c < a:
            return 2
        else:
            return 3


a, b, c = map(int, input().split()) # эту строчку не менять
# здесь создайте экземпляр tr класса TriangleChecker и вызовите метод is_triangle() с выводом информации на экран
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())

#assert
assert isinstance(tr, TriangleChecker) and hasattr(TriangleChecker, 'is_triangle')


def is_triangle(a, b, c):
    for x in (a, b, c):
        if type(x) not in (int, float):
            return 1

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a < (b + c) and b < (a + c) and c < (a + b):
        return 3

    return 2


assert tr.is_triangle() == is_triangle(a, b,
                                       c), f"неверный возвращаемый код методом is_triangle(a, b, c): {tr.is_triangle()}, а должен {is_triangle(a, b, c)}"

try:
    tr = TriangleChecker('3', 4, 5)
except TypeError:
    assert False, "При передаче нечисловых аргументов команда TriangleChecker(arg1, arg2, arg3) выдает ошибку"

assert tr.is_triangle() == is_triangle('3', 4,
                                       5), f"неверный возвращаемый код методом is_triangle('3', 4, 5) при наличии нечисловых аргументов: {tr.is_triangle()}, а должен {is_triangle('3', 4, 5)}"

tr = TriangleChecker(3.0, 4.0, 5.0)
assert tr.is_triangle() == is_triangle(3.0, 4.0,
                                       5.0), f"неверный возвращаемый код методом is_triangle при вещественных аргументах: {tr.is_triangle()}, а должен {is_triangle(3.0, 4.0, 5.0)}"