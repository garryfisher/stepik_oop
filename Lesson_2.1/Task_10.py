import random


class EmailValidator:
    SYMBOL = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@._'
    GEN_SYM = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@._'

    def __new__(cls, *args, **kwargs):
        if cls is EmailValidator:
            return None
        return object.__new__(cls)

    @classmethod
    def get_random_email(cls):
        len_ = random.randint(0, 65)
        part1 = ''
        for x in range(len_):
            x = random.choice(cls.GEN_SYM)
            part1 += x
        return part1 + '@gmail.com'

    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email):
            if not email.count('@') == 1:
                return False
            if '..' in email:
                return False
            for x in email:
                if x not in cls.SYMBOL:
                    return False
            lst = email.split('@')
            if not len(lst[0]) <= 100 or not len(lst[1]) <= 50:
                return False
            if lst[1].count('.') < 1:
                return False
            if lst[1][-1] == '.':
                return False
        else:
            return False

        return True

    @staticmethod
    def __is_email_str(email):
        return type(email) == str