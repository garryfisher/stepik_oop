class Server:
    addr = list()

    def __new__(cls):
        if len(cls.addr) == 0:
            cls.addr.append(1)
        else:
            cls.addr.append(cls.addr[-1] + 1)
        return super().__new__(cls)

    def __init__(self):
        self.data = None
        self.cache = None
        self.ip = Server.addr[-1]
        self.buffer = list()

    def send_data(self, data):
        self.data = data
        rt_buffer = Router.buffer
        rt_buffer.append(data)

    def get_data(self):
        if len(self.buffer) == 0:
            return []
        else:
            self.cache = self.buffer[:]
            self.buffer.clear()
            return self.cache

    def get_ip(self):
        return self.ip


class Router:
    buffer = []
    arp = {}

    def link(self, server):
        self.arp[server.ip] = server

    def unlink(self, server):
        self.arp.pop(server.ip)

    def send_data(self):
        for ip in self.arp:
            for item in self.buffer:
                if item.ip != ip:
                    continue
                else:
                    self.arp[ip].buffer.append(item)
        self.buffer.clear()


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


#assert
assert hasattr(Router, 'link') and hasattr(Router, 'unlink') and hasattr(Router, 'send_data'), "в классе Router присутсвутю не все методы, указанные в задании"
assert hasattr(Server, 'send_data') and hasattr(Server, 'get_data') and hasattr(Server, 'get_ip'), "в классе Server присутсвутю не все методы, указанные в задании"

router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

assert len(router.buffer) == 0, "после отправки сообщений буфер в роутере должен очищаться"
assert len(sv_from.buffer) == 0, "после получения сообщений буфер сервера должен очищаться"

assert len(msg_lst_to) == 2, "метод get_data вернул неверное число пакетов"

assert msg_lst_from[0].data == "Hi" and msg_lst_to[0].data == "Hello", "данные не прошли по сети, классы не функционируют должным образом"

assert hasattr(router, 'buffer') and hasattr(sv_to, 'buffer'), "в объектах классов Router и/или Server отсутствует локальный атрибут buffer"

router.unlink(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
router.send_data()
msg_lst_to = sv_to.get_data()
assert msg_lst_to == [], "метод get_data() вернул неверные данные, возможно, неправильно работает метод unlink()"
