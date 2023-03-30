class ValidateString:
    def __init__(self, min_length=3, max_length=100):
        self.min_ = min_length
        self.max_ = max_length

    def validate(self, string):
        return type(string) == str and self.min_ <= len(string) <= self.max_


class StringValue:
    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)


class RegisterForm:
    login = StringValue(ValidateString())
    password = StringValue(ValidateString())
    email = StringValue(ValidateString())

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print(f'<form> \n'
              f'Логин: {self.login}\n'
              f'Пароль: {self.password}\n'
              f'Email: {self.email}\n'
              f'</form>')