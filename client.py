import socket

def client():
    host = '0.0.0.0'  #Mesma coisa que o server.py,
    port = 18000         #Porta 1000 não funcionava

    client_socket = socket.socket()
    print(f"Attempting to connect to server at {host}:{port}") #Debugs de teste
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}") #Debugs de teste, conexão successful

    while True:
        #Mandar mensagem para o server
        message = input("Enter message for server -> ")
        #if message.lower() == 'bye':
        #    print("Closing connection.")
        #    break

        #client_socket.send(message.encode())  
        #print(f"Sent to server: {message}")

        #Receber resposta do servidor
        data = client_socket.recv(1024).decode()
        print(f"Received from server: {data}")

    client_socket.close()

if __name__ == '__main__':
    client()