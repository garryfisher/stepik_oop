import random


class Line:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.sp = a, b
        self.ep = c, d


class Rect:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.sp = a, b
        self.ep = c, d


class Ellipse:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.sp = a, b
        self.ep = c, d


classes_lst = [Line, Rect, Ellipse]
r_num = random.randint(1, 100)
elements = [random.choice(classes_lst)(r_num, r_num, r_num, r_num) for _ in range(217)]
for x in elements:
    if isinstance(x, Line):
        x.a, x.b, x.c, x.d = 0, 0, 0, 0
        x.sp, x.ep = (0, 0), (0, 0)


#assert
assert len(elements) == 217

for e in elements:
    assert isinstance(e, Line) or isinstance(e, Rect) or isinstance(e, Ellipse), "в списке elements должны быть только объекты классов Line, Rect, Ellipse"

l = Line(1, 2, 3, 4)
assert l.sp == (1, 2) and l.ep == (3, 4), "неверные значения в атрибутах sp, ep класса Line"

for e in elements:
    if isinstance(e, Line):
        assert e.sp == (0, 0) and e.ep == (0, 0), "в объектах класса Line координаты должны быть равны нулю"
