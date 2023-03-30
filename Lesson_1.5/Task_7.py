# здесь пишите программу
class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, *mems):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = mems[:self.total_mem_slots]

    def get_config(self):
        return [f'Материнская плата: {self.name}',
                f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                'Память: ' + "; ".join(map(lambda x: f"{x.name} - {x.volume}", self.mem_slots))]


mb = MotherBoard('Giga', CPU('Asus', 1333), Memory('Kingstone', 4000), Memory('Kingstone', 4000))

#assert
assert isinstance(mb, MotherBoard) and hasattr(MotherBoard, 'get_config')


def get_config():
    mem_str = "; ".join([f"{x.name} - {x.volume}" for x in mb.mem_slots])

    return [f"Материнская плата: {mb.name}",
            f"Центральный процессор: {mb.cpu.name}, {mb.cpu.fr}",
            f"Слотов памяти: {mb.total_mem_slots}",
            f"Память: {mem_str}"]


res1 = ("".join(mb.get_config())).replace(" ", "")
res2 = ("".join(get_config())).replace(" ", "")
assert res1 == res2, "метод get_config возвратил неверные данные"