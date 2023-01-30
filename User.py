class User:
    def __init__(self, network):
        self.id = network.id
        self.points = 10
        self.user_text = ["", ""]
        self.users = ","

    def update_points(self):
        self.points -= 1

    def update_text(self, text, network, interface):
        self.text = text
        self.send_text(text, network, interface)

    def transform_list(self, text):
        t1 = text[0]
        t2 = text[1]
        return t1 + "," + t2

    def convert_list(self):
        return self.users

    def send_text(self, text, network, interface):
        self.users = network.send(self.transform_list(text))
        # self.convert_list(interface)
