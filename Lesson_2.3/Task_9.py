class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = list()
        self.current_weight = 0

    @property
    def things(self):
        return self.__things

    def add_thing(self, things):
        if self.current_weight < self.max_weight \
                and self.max_weight - things.weight > 0:
            self.things.append(things)
            self.current_weight += things.weight

    def remove_thing(self, indx):
        self.__things.pop(indx)

    def get_total_weight(self):
        return self.current_weight


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight