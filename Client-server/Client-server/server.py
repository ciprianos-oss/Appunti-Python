import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 5000))

server.listen()

print("Server in attesa...")

connessione, indirizzo = server.accept()

print("Client collegato:", indirizzo)

messaggio = connessione.recv(1024).decode()

print("Messaggio ricevuto:", messaggio)

connessione.send("Ciao client!".encode())

connessione.close()
server.close()