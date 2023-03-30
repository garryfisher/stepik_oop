class PathLines:
    def __init__(self, *args):
        self.lst_obj = list()
        if args:
            if isinstance(args, (tuple, list)):
                for x in args:
                    self.lst_obj.append(x)
            else:
                self.lst_obj.append(args)


    def get_path(self):
        return self.lst_obj

    def add_line(self, line):
        self.lst_obj.append(line)

    def get_length(self):
        L = 0
        x0 = y0 = 0
        for obj in self.lst_obj:
            L += ((obj.x - x0) ** 2 + (obj.y - y0) ** 2) ** 0.5
            x0, y0 = obj.x, obj.y

        return L


class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y