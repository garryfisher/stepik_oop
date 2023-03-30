from string import ascii_lowercase, digits


# здесь объявляйте классы TextInput и PasswordInput
class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    @classmethod
    def check_name(cls, name):
        flag = None
        flag = True if 3 <= len(name) <= 50 else False
        if flag:
            for x in name:
                if x not in cls.CHARS_CORRECT:
                    return False
        return flag

    def __init__(self, name, size=10):
        self.name = name
        self.size = size
        if not self.check_name(self.name):
            raise ValueError("некорректное поле name")

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"


class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    @classmethod
    def check_name(cls, name):
        flag = None
        flag = True if 3 <= len(name) <= 50 else False
        if flag:
            for x in name:
                if x not in cls.CHARS_CORRECT:
                    return False
        return flag

    def __init__(self, name, size=10):
        self.name = name
        self.size = size
        if not self.check_name(self.name):
            raise ValueError("некорректное поле name")

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()

#assert
assert isinstance(login, FormLogin)


class TextInput2:
    def __init__(self, name, size=10):
        self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"


class PasswordInput2:
    def __init__(self, name, size=10):
        self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"


f1_1 = TextInput("Login123")
f1_2 = PasswordInput("Psw")

f2_1 = TextInput2("Login123")
f2_2 = PasswordInput2("Psw")

f11 = f1_1.get_html().replace(' ', '').replace('\'', '"')
f12 = f1_2.get_html().replace(' ', '').replace('\'', '"')
f21 = f2_1.get_html().replace(' ', '').replace('\'', '"')
f22 = f2_2.get_html().replace(' ', '').replace('\'', '"')
assert f11 == f21 and f12 == f22, "неверное возвращаемое значение методом get_html"

try:
    a = TextInput('aa')
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    a = PasswordInput('aa')
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"
