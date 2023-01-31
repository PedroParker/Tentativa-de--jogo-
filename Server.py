import socket
from _thread import start_new_thread


class Server:
    def __init__(self):
        self.host = "localhost"
        self.port = 5000
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listen = 2
        self.connected = 0
        self.connections = []
        self.server_program()

    # Initializer -------------------------------------------------------------

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

    # Client holder -----------------------------------------------------------

    def thread_client(self, conn):
        self.make_connection(conn)

        while True:
            try:
                data = conn.recv(1024).decode("utf-8")
                print(data)
                self.broadcast(conn, data)
                if not data:
                    break
            except socket.error:
                break

        self.close_connection(conn)

    # Connection administrating -----------------------------------------------

    def close_connection(self, conn):
        print("Fechando conexão")
        self.connected -= 1
        conn.close()

    def make_connection(self, conn):
        self.connected += 1
        self.connections.append(conn)
        return self.connected

    # Sync information --------------------------------------------------------

    def broadcast(self, conn, data):
        for client in self.connections:
            if client != conn:
                try:
                    client.send(data.encode("utf-8"))
                except socket.error:
                    self.close_connection(client)
                    self.connections.remove(client)


server = Server()
