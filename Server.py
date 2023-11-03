from socket import *
from threading import *
 
clients = []
names = []
 
def clientThread(client):
    bayrak = True
    while True:
        try:
            message = client.recv(1024).decode('utf8')
            if bayrak:
                names.append(message)
                print(message, 'bağlandi')
                bayrak = False
            for c in clients:
                if c != client:
                    index = clients.index(client)
                    name = names[index]
                    c.send((name + ':' + message).encode('utf8'))
        except:
            index = clients.index(client)
            clients.remove(client)
            name=names[index]
            names.remove(name)
            print(name + ' çikti')
            break
 
 
server = socket(AF_INET, SOCK_STREAM)
 
ip = '124.208.44.205'
port = 6667
server.bind((ip, port))
server.listen()
print('Server dinlemede...')
 
 
while True:
    client, address = server.accept()
    clients.append(client)
    print('Bağlantı yapıldı..', address[0] + ':' + str(address[1]))
    thread = Thread(target=clientThread, args=(client, ))
    thread.start()
    
    