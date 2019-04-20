import socket
import json
from coordinator import Coordinator
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 32132)
print('Starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(5)
c = Coordinator()

while True:
    connection, client_address = sock.accept()
    #print('connection from', client_address)
    # Receive the data 
    data_string = connection.recv(4096)
    #print('received {!r}'.format(data_string))
    if data_string:
        #Parsed Json
        p = json.loads(data_string)
        print(p)
        if(p['open'] == True):
            print('open_trans')
            r = c.open_trans()
            print('open_trans data',r)
            connection.sendall(str(r))

        # elif(p['token'] == None and p['action']=='get_balance'):
        #     print('DIRTY READ')
        #     r = c.do(p['token'], p['action'] )
        #     print(r)
        #     connection.sendall(str(r))

        elif(p['token']):
            print('Do::')
            r = c.do(p['token'], p['action'], p['params'] )
            print(r)
            connection.sendall(str(r))

    else:
        print('no data from', client_address)

