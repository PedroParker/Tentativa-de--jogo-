import socket
from _thread import start_new_thread


class Server:
    def __init__(self):
        self.host = "localhost"
        self.port = 5000
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listen = 2
        self.connected = 0
        self.users_text = [","]
        self.server_program()

    def server_program(self):
        self.server.bind((self.host, self.port))
        self.server.listen(self.listen)
        while True:
            try:
                conn, address = self.server.accept()
                print("Connection from: " + str(address))
                start_new_thread(self.thread_client, (conn,))
            except KeyboardInterrupt:
                print("Quebrando servidor")
                break

    def thread_client(self, conn):
        player = self.make_connection(conn)
        while True:
            try:
                data = conn.recv(2048).decode()
                if not data:
                    break
                self.users_text[player - 1] = data
                conn.sendall(str.encode(self.users_text[1]))
            except socket.error:
                break
        print("Fechando conexão")
        self.close_connection(conn)

    def close_connection(self, conn):
        self.connected -= 1
        conn.close()

    def make_connection(self, conn):
        self.connected += 1
        conn.send(str.encode(f"{self.connected}"))
        self.users_text.append(",")
        return self.connected


server = Server()
