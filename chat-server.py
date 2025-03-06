import socket
import threading


HOST = '127.0.0.1'
PORT = 12345


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

def broadcast(message, sender_client):
    for client in clients:
        if client != sender_client:
            client.send(message)

def handle_client(client):
    while True:
        message = client.recv(1024)

        if not message:
            break

        broadcast(message, client)  
              
    index = clients.index(client)
    clients.remove(client)
    nickname = nicknames.pop(index)
    broadcast(f"{nickname} has left the chat.".encode(), client)
    client.close()

def receive_connections():
    print("Server is running and listening...")
    while True:
        client, addr = server.accept()
        print(f"Connected with {str(addr)}")

        client.send("NICK".encode())
        nickname = client.recv(1024).decode()
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname: {nickname}")
        broadcast(f"{nickname} joined the chat!".encode(), client)
        client.send("Connected to the chat!".encode())

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive_connections()