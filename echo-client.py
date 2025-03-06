import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        while True:
            msg = input("Enter Your Message: ")

            if msg == "exit":
                break
            
            s.sendall(msg.encode())
            data = s.recv(1024)
        
            print(f'Data Received from Server: "{data.decode()}"')
    except ConnectionRefusedError:
        print("Server is not running.")
