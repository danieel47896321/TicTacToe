import socket
from _thread import start_new_thread
from board import Board
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "192.168.14.128"
port = 1000
s.bind((server, port))
s.listen()
print("| -- Server is Online -- |")
connections = 0
games = {0:Board(3, 3)}
users = {}

def threaded_client(conn, game):
    global pos, games, currentId, connections
    try:
        bo = games[game]
        if connections % 2 == 0:
            currentId = "player1"
        else:
            currentId = "player2"
        bo.start_user = currentId
        # Pickle the object and send it to the server
        data_string = pickle.dumps(bo)
        if currentId == "player2":
            bo.ready = True
        conn.send(data_string)
        connections += 1
        while True:
            d = conn.recv(8192 * 3)
            data = d.decode("utf-8")

            if data.count("select") > 0:
                all = data.split(" ")
                row = int(all[1])
                col = int(all[2])
                player = all[3]
                bo.select(row, col, player)
                
            if data == "winner player2":#print to the server who is the winer
                bo.winner = "player2"
                print("Player2 won in game", game)
                
            if data == "winner player1":#print to the server who is the winer
                bo.winner = "player1"
                print("Player1 won in game", game)
                  
            sendData = pickle.dumps(bo) #recive from board
            conn.sendall(sendData) #send to player
        del games[game]
        connections -= 1
        print("Game ",game," Ended")
        conn.close()  
    except: #defend from attacks
        connections -= 1
        conn.close()
        
def dos_protect(conn,addr):
    global users
    if addr[0] not in users:
        users = {addr[0]:1}
    else:
        users = {addr[0]:users[addr[0]]+1}
    if users[addr[0]]>10:
        conn.close()
    
while True:
    conn, addr = s.accept() #accept the connection
    dos_protect(conn,addr)
    print("connection to ",addr)
    index = -1
    for game in games.keys():
        if games[game].ready == False:
            index = game
    if index == -1:
        try:
            index = list(games.keys())[-1]+1
            games[index] = Board(3,3)
        except:
            index = 0
            games[index] = Board(3,3)
    print("Number of Connections:", connections+1)
    print("Number of Games:", len(games))
    start_new_thread(threaded_client, (conn,index))