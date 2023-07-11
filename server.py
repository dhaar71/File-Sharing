import socket

def start_server():
    host = socket.gethostname()
    port = 8080

    s = socket.socket()
    s.bind((host, port))
    s.listen(1)

    print(f"Server started. Listening on {host}:{port}")

    while True:
        conn, addr = s.accept()
        print(f"Incoming connection from {addr[0]}:{addr[1]}")

        file = open("received_file.txt", "wb")

        while True:
            file_data = conn.recv(1024)
            if not file_data:
                break
            file.write(file_data)

        file.close()
        print("File has been received successfully")

        conn.close()

start_server()
