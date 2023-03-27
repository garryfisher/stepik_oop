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
