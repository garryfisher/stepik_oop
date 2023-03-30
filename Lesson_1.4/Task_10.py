class Translator:
    dictionary = dict()

    def add(self, eng, rus):
        if eng not in self.dictionary:
            self.dictionary[eng] = [rus]
        if rus not in self.dictionary[eng]:
            self.dictionary[eng].append(rus)

    def remove(self, eng):
        self.dictionary.pop(eng, None)

    def translate(self, eng):
        if eng in self.dictionary:
            return self.dictionary[eng]
        else:
            return f'Meaning "{eng}" absent from the dictionary'


tr = Translator()
tr.add('tree', 'дерево')
tr.add('car', 'машина')
tr.add('car', 'автомобиль')
tr.add('leaf', 'лист')
tr.add('river', 'река')
tr.add('go', 'ехать')
tr.add('go', 'идти')
tr.add('go', 'ходить')
tr.add('milk', 'молоко')
tr.remove('car')
print(*tr.translate('go'))

#assert
assert isinstance(tr, Translator)
assert hasattr(Translator, 'add') and hasattr(Translator, 'remove') and hasattr(Translator, 'translate')
assert tr.translate('tree')[0] == "дерево"
