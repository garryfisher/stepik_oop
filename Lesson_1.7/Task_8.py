from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits + ' '

    @classmethod
    def check_card_number(cls, number):
        if type(number) != str:
            return False
        if len(number) != 19:
            return False
        else:
            for x in range(len(number)):
                if not number[x].isdigit() and x not in (4, 9, 14):
                    return False
                elif x in (4, 9, 14) and number[x] != '-':
                    return False
        return True

    @classmethod
    def check_name(cls, name):
        if type(name) != str:
            return False
        result = name.split()
        if len(result) != 2:
            return False
        for x in name:
            return False if x not in cls.CHARS_FOR_NAME else True
        return False
