import socket

def server():
    host = '127.0.0.1'
    port = 5000  #Porta 1000 não estava a funcionar localmente,
                 #Corri o código com $ sudo python3 server.py/client.py
    server_socket = socket.socket()
    server_socket.bind((host, port))
    print(f"Server started, listening on {host}:{port}") #Debugs de testes

    server_socket.listen(1)
    conn, address = server_socket.accept()
    print(f"Connection accepted from {address}") #Mais debugs, conexão successful aqui

    while True:
        #"Ouvir" o cliente
        data = conn.recv(1024).decode()
    #    if not data:
    #        print("No data received. Closing connection.")
    #        break

        print(f"Received from client: {data}")

        #Responder ao cliente
        data = input('Enter response to client -> ')
        conn.send(data.encode())

    conn.close()

if __name__ == '__main__':
    server()