class Viber:
    msg_list = dict()

    @classmethod
    def add_message(cls, msg):
        cls.msg_list[msg.text] = [msg.text, msg.fl_like]

    @classmethod
    def remove_message(cls, msg):
        cls.msg_list.pop(msg.text)

    @staticmethod
    def set_like(msg):
        msg.fl_like = False if msg.fl_like else True

    @classmethod
    def show_last_message(cls, num):
        print(cls.msg_list[-num:])

    @classmethod
    def total_messages(cls):
        return len(cls.msg_list)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like

#assert
assert hasattr(Viber, 'show_last_message'), "отсутствует метод show_last_message"

msg = Message("Всем привет!")
Viber.add_message(msg)
assert Viber.total_messages() == 1, "сообщение не было добавлено: некорректно работает метод add_message"

Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
assert Viber.total_messages() == 3, "неверное число сообщений: некорректно работает метод add_message"

assert msg.fl_like == False, "лайка по умолчанию не должно быть - значение False"
Viber.set_like(msg)
assert msg.fl_like == True, "лайк не проставился: некорректно работает метод set_like"
Viber.set_like(msg)
assert msg.fl_like == False, "лайк не убрался при повторном вызове метода set_like"
Viber.remove_message(msg)

assert Viber.total_messages() == 2, "неверное число сообщений: некорректно работает метод remove_message"