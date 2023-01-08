import socket

# dictionary amiben a kliensek kulcsait tároljuk
clients = {}

# kvoetkezo kliens ID-ja
next_client_id = 8001

# socket amin keresztul a kliensekkel kommunikalunk
server_socket = socket.socket()
server_socket.bind(('localhost', 8000))
server_socket.listen()

while True:
    # fogadjuk a klienseket a socketen keresztul
    client_socket, client_address = server_socket.accept()

    # fogadjuk a kliens kéréseit
    request = client_socket.recv(1024).decode('utf-8')

    # feldolgozzuk a kéréseket
    request_parts = request.split()
    # ha az uzenet elejen req van akkor a kliens valakinek a kulcsat keri
    if request_parts[0] == 'req':
        # az uzenet masodik resze a keresett kliens ID-ja
        client_id = request_parts[1]
        if client_id in clients:
            # visszateritjuk a kliensnek a keresett kulcsot
            client_socket.send(clients[client_id].encode('utf-8'))
        else:
            # Ha a kliens nem létezik akkor hibauzenetet küldünk    
            client_socket.send('Kliens nincs a rendszerben'.encode('utf-8'))
    # ha az uzenet elejen su van akkor a kliens kulcsot küld (su = sign up)
    elif request_parts[0] == 'su':
        # az uzenet masodik resze a kliens ID-ja
        client_id = request_parts[1]
        # az uzenet harmadik resze a kliens kulcsa
        public_key = request_parts[2]
        if client_id in clients.keys():
            # ha a kliens ID már létezik a rendszewrben, frissitjuk a kulcsot
            clients[client_id] = public_key
            client_socket.send('Kiliens id mar letezik, kulcs frissitve'.encode('utf-8'))
        else:
            # ha a kliens ID nem létezik a rendszerben, hozzáadjuk
            clients[client_id] = public_key
            client_socket.send(str(next_client_id).encode('utf-8'))
            # Increment the next available client ID
            next_client_id += 1
        # Store the client ID and public key    
    else:
        # Invalid request
        client_socket.send('Invalid request'.encode('utf-8'))

    # Close the client socket
    client_socket.close()
