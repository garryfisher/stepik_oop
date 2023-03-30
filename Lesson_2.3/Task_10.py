class TVProgram:
    def __init__(self, name):
        self.name = name
        self.items = list()

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx):
        for x in self.items:
            if x.uid == indx:
                self.items.remove(x)


class Telecast:
    def __init__(self, indx, name, duration):
        self.__id = indx
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, indx):
        self.__id = indx

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, indx):
        self.__name = indx

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, indx):
        self.__duration = indx