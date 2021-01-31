import socket
import pickle
import struct
class Network:
    def __init__(self):
        self.client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server="192.168.0.105"
        self.port=5555
        self.addr=(self.server,self.port)
        self.p=self.connect()
    def getP(self):
        return self.p       
        
    def connect(self):
        try:
            self.client.connect_ex(self.addr)
            return pickle.loads(self.client.recv(4096))
        except:
            pass
    def send(self,data):
        try:
            self.client.send(pickle.dumps(data))
            a=self.client.recv(8192)
            print(a)
            return pickle.loads(a)
        except socket.error as e:
            print(e)

