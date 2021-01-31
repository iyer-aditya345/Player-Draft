import socket
import sys
import pickle
from _thread import *
from player import Player
server="192.168.0.105"
port = 5555

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.bind((server,port))
except socket.error as e:
    str(e)
    print(e)
s.listen()
print("waiting for connection,Server Started")


players = [Player(0,0,50,50,(255,0,0)),Player(0,0,100,100,(0,0,255))]
def threaded_client(conn,player):
    
    conn.send(pickle.dumps(players[player]))
    reply=""
    while True:
        try:
            data=pickle.load(conn.recv(4096))
            players[player]=data

            if not data:
                print("Disconnected")
                break
            else:
                if player==1:
                    reply=players[0]
                else:
                    reply=players[1]

                print("Recieved",data)
                print("sending:",reply)
            conn.sendall(pickle.dumps(reply))
        except:
            break
    print("Lost Connection")
    conn.close()    

currentplayer=0


while True:
    conn,addr=s.accept()
    print(conn,"Connected to:",addr)
    start_new_thread(threaded_client,(conn,currentplayer))
    currentplayer+=1
