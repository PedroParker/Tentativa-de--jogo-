import socket
from _thread import start_new_thread


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "localhost"
        self.port = 5000
        self.address = (self.host, self.port)
        self.connect()
        self.data = ","

    # Initializer ------------------------------------------------------------------

    def connect(self):
        try:
            self.client.connect(self.address)
            start_new_thread(self.recive, ())
        except socket.error:
            print("Failed establishing connection")

    # Connection administrator ------------------------------------------------

    def disconnect(self):
        print("Disconnected")
        self.client.close()

    # Sync information --------------------------------------------------------

    def send(self, data):
        try:
            self.client.sendall(data.encode("utf-8"))
        except socket.error:
            print("Connection failed, possibly the server is dead")

    def recive(self):
        while True:
            try:
                self.data = self.client.recv(1024).decode("utf-8")
                if not self.data:
                    break
            except socket.error:
                break
        self.disconnect()

    # Getters -----------------------------------------------------------------

    def get_data(self):
        return self.data
