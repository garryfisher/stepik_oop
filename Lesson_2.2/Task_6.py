class Stack:

    def __init__(self):
        self.top = None
        self.end = None

    def push(self, obj):
        if self.end:
            self.end.next = obj
        self.end = obj
        if not self.top:
            self.top = obj

    def pop(self):
        t = self.top
        if not t:
            return
        while t and t.next != self.end:
            t = t.next
        if t:
            t.next = None
        end = self.end
        self.end = t
        if self.end is None:
            self.top = None
        return end

        return last

    def get_data(self):
        lst = []
        t = self.top
        while t:
            lst.append(t.data)
            t = t.next
        return lst


class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_):
        self.__next = next_ if isinstance(next_, StackObj) or next_ is None else None
