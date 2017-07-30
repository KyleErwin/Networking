from Database import displayMenu
import socketserver

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class server(socketserver.StreamRequestHandler):
    def handle(self):
        while True:
            displayMenu(self)
            return;

    def write(self, string):
        self.wfile.write(bytearray(string, "utf-8"))

    def read(self):
        return self.rfile.readline().strip().decode("utf-8")


if __name__ == '__main__':
    port = 8007
    print("Server Started!")
    print("Listening on localhost:{}".format(port))

    server = ThreadedTCPServer(("localhost", int(port)), server)

    try:
        server.serve_forever()
    finally:
        server.shutdown()
        server.server_close()