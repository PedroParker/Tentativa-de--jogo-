from Network import Network


class User:
    def __init__(self):
        self.network = Network()
        self.text = ""
        self.data = ""

    # Methods ------------------------------------------------------------------

    def update_data(self):
        self.data = self.network.get_data()
        return self.data

    def send_text(self):
        self.network.send(self.text)

    # Setters -----------------------------------------------------------------

    def set_text(self, text):
        self.text = text
        self.send_text()

    # Getters -----------------------------------------------------------------

    def get_text(self):
        return self.text
