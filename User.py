from Network import Network


class User:
    def __init__(self):
        self.network = Network()
        self.text = ["", ""]
        self.data = ["", ""]

    # Methods ------------------------------------------------------------------

    def update_data(self):
        self.data = self.network.get_data().split(",")
        print(self.data)
        return self.data

    def send_text(self):
        text = self.text[0] + "," + self.text[1]
        self.network.send(text)

    # Setters -----------------------------------------------------------------

    def set_text(self, text, id):
        self.text[id - 1] = text
        self.send_text()

    # Getters -----------------------------------------------------------------

    def get_text(self):
        return self.text
