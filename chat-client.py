import socket
import threading

HOST = '127.0.0.1'
PORT = 12344

nickname = input("Enter your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == "NICK":
                client.send(nickname.encode())
            else:
                print(message)
        except:
            print("Disconnected from the server.")
            client.close()
            break

def send_messages():
    while True:
        message = input()

        if message == "exit":
            client.send("{nickname} has left the chat".encode())
            client.close()
            break

        client.send(f"{nickname}: {message}".encode())

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()