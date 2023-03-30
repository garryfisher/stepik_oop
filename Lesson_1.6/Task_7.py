# здесь объявляйте класс SingletonFive
class SingletonFive:
    name = []

    def __new__(cls, *args, **kwargs):
        if len(cls.name) <= 4:
            cls.name.append(super().__new__(cls))
        return cls.name[-1]


objs = [SingletonFive(str(n)) for n in range(10)] # эту строчку не менять