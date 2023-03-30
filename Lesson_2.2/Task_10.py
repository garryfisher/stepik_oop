class PhoneBook:
    def __init__(self):
        self.lst_phone = list()

    def add_phone(self, phone):
        self.lst_phone.append(phone)

    def remove_phone(self, indx):
        self.lst_phone.pop(indx)

    def get_phone_list(self):
        result = list()
        for x in self.lst_phone:
            result.append(x)
        return result


class PhoneNumber:
    def __init__(self, number, fio):
        self.number = number
        self.fio = fio
