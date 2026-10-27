import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("0.0.0.0", 5000))

while(1):
    server.listen()

    print("Server in attesa...")

    connessione, indirizzo = server.accept()

    print("Client collegato:", indirizzo)

    richiesta = connessione.recv(4096).decode("utf-8")

    print("Richiesta ricevuta:")
    print(richiesta)

    risposta = """HTTP/1.1 200 OK
    Content-Type: text/html; charset=utf-8

    <h1>Ciao dal mio server Python!</h1>
    <p>Il server funziona.</p>

    """

    connessione.send(risposta.encode("utf-8"))
    print(indirizzo[0])
    if indirizzo[0] == "10.11.23.8":
        print("e' lui")
        risposta  = """<h1> Ciao Cipriano </h1>"""
        connessione.send(risposta.encode("utf-8"))
    if indirizzo[0] == "10.11.23.7":
        print("e' lei")
        risposta  = """<h1> Ciao Serena </h1>"""
        connessione.send(risposta.encode("utf-8"))
connessione.close()
server.close()