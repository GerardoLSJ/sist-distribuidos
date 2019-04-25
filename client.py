import socket
import time
import json
import threading

lock = threading.Lock()

server_address = ('localhost', 4444)

class Client():
    def __init__(self,name):
        self.name = name
        self.sock = None
        self.token = None
        self.request = { 'token': None, 'action': None, 'params':None }
        #self.open_session()
        
    def open_sock(self):
        #print('open sock')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(server_address)

    def close_sock(self):
        self.sock.close()
        #print('close sock')

    def open_session(self):
        self.open_sock()
        self.request = {'open':True}
        json_str = json.dumps(self.request, separators=(',', ':'))
        self.sock.send(json_str)
        token = self.sock.recv(4096)
        if(len(token) == 8):
            self.token = token
            print('open sess',self.token,self.name)
        else:
            self.token = None
            print('error',token,self.name)
                
        self.close_sock()

    def close_session(self):
        #print('close')
        self.open_sock()
        self.request = {'token':self.token, 'action':'close_session', 'params':None, 'open':False}
        json_str = json.dumps(self.request, separators=(',', ':'))
        self.sock.send(json_str)
        reply = self.sock.recv(4096)
        self.close_sock()
        print('close_session', reply, self.name)

    def get_balance(self):
        self.open_sock()
        self.request = {'token':self.token, 'action':'get_balance', 'params':None,'open':False}
        json_str = json.dumps(self.request, separators=(',', ':'))
        self.sock.send(json_str)
        reply = self.sock.recv(4096)
        print('Get Balance: ',self.name, reply,self.token)
        self.close_sock()
        
    def increase(self, porcentage):
        self.open_sock()
        self.request = {'token':self.token, 'action':'increase', 'params':porcentage,'open':False}
        json_str = json.dumps(self.request, separators=(',', ':'))
        self.sock.send(json_str)
        reply = self.sock.recv(4096)
        print('Increase: ',self.name,reply,self.token)
        self.close_sock()

    def deposit(self, amount):
        self.open_sock()
        self.request = {'token':self.token, 'action':'deposit', 'params':amount,'open':False}
        json_str = json.dumps(self.request, separators=(',', ':'))
        self.sock.send(json_str)
        reply = self.sock.recv(4096)
        print('Deposit: ',self.name, reply,self.token)
        self.close_sock()

    def withdraw(self, amount):
        self.open_sock()
        self.request = {'token':self.token, 'action':'withdraw', 'params':amount, 'open':False}
        json_str = json.dumps(self.request, separators=(',', ':'))
        self.sock.send(json_str)
        reply = self.sock.recv(4096)
        print('Withdraw: ',self.name,reply,self.token)
        self.close_sock()

    

#x = Client('Bob')
a = Client('Alice')
#x.open_session()
a.open_session()
a.withdraw(100)
a.get_balance()

time.sleep(3)
a.close_session()

x = Client('Bob')
x.open_session()
x.get_balance()

# a.get_balance()

# #a.close_session()
# #x.close_session()
# #a.withdraw(10)
# a.get_balance()
# a.close_session()
