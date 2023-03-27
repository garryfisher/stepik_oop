# Объявите класс с именем MediaPlayer с двумя методами:
#
# open(file) - для открытия медиа-файла с именем file (создает локальное свойство filename со значением аргумента file в объекте класса MediaPlayer)
# play() - для воспроизведения медиа-файла (выводит на экран строку "Воспроизведение <название медиа-файла>")
#
# Создайте два экземпляра этого класса с именами: media1 и media2. Вызовите из них метод open() с аргументом "filemedia1" для объекта media1 и "filemedia2" для объекта media2. После этого вызовите через объекты метод play(). При этом, на экране должно отобразиться две строки (без кавычек):
#
# "Воспроизведение filemedia1"
# "Воспроизведение filemedia2"


class MediaPlayer:
    def open(self, file):
        setattr(self, 'filename', file)

    def play(self, filename):
        print(f'Воспроизведение {filename}')


media1 = MediaPlayer()
media2 = MediaPlayer()
media1.open('filemedia1')
media2.open('filemedia2')
media1.play(media1.__dict__['filename'])
media2.play(media2.__dict__['filename'])
