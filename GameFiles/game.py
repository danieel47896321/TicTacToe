import pygame,time
from client import Network
import os
pygame.font.init()
#photos
board = pygame.transform.scale(pygame.image.load(os.path.join("img","board.jpg")), (750, 750))
open_screen = pygame.image.load(os.path.join("img", "open.jpg"))
off_screen = pygame.image.load(os.path.join("img", "offline.jpg"))

rect = (113,113,525,525)
turn = "player1"
#some colors
Blue=(0,0,255)
White=(255,255,255)
Red=(255, 0, 0)

def menu_screen(win): #1
    global bo
    run = True
    offline = False # false = server online
    while run:
        if not offline: #server online
            win.blit(open_screen,(0,0))
        pygame.display.update()
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:#check if we click on exit
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN: #check if we click on screen
                offline = False
                try: #try to connect and stat the game
                    bo = connect()
                    run = False
                    main()
                    break
                except: #server offline
                    offline = True
                    win.blit(off_screen,(0,0))

def end_screen(text): #print who is win and wait 1 sec
    Print(text,Blue,60,400,300)
    pygame.display.update()
    time.sleep(1)
            
def connect(): #connect to the server
    global n
    n = Network()
    return n.board

def Print(text,color,font_size,cord1,cord2):#function to print for the user
    latgetext=pygame.font.Font('freesansbold.ttf',font_size) #font and size
    textSurface=latgetext.render(text,True,color)
    TextRect=textSurface.get_rect()
    TextRect.center=(cord1,cord2)
    win.blit(textSurface,TextRect) #display the text
    
def userWindow(win, bo, player, ready): #print info to the users
    win.blit(board, (0, -100))
    bo.draw(win)
    if not ready:
        Print("waiting for opponent",Blue,60,375,300)
    if ready:
        Print("press q to quit",Blue,30,600,20)
    if not player == "s":
        if player == "player1":
            Print("you are Player1",Blue,30,140,20)
        else:
            Print("you are Player2",Blue,30,140,20)
        if bo.turn == player:
            Print("your turn",Red,30,380,20)
        else:
            Print("opponent turn",Red,30,370,20)
    pygame.display.update()

def click(pos): #get the click cords and return it
    x = pos[0]
    y = pos[1]
    #first row
    if 110 < x < 300 and 40 < y < 190:
        return 0,0
    if 320 < x < 435 and 40 < y < 180:
        return 0,1
    if 470 < x < 640 and 40 < y < 180:
        return 0,2
    #second row
    if 100 < x < 290 and 225 < y < 380:
        return 1,0
    if 315 < x < 450 and 210 < y < 390:
        return 1,1
    if 490 < x < 630 and 210 < y < 400:
        return 1,2
    #third row
    if 70 < x < 270 and 420 < y < 570:
        return 2,0
    if 310 < x < 465 and 430 < y < 570:
        return 2,1
    if 500 < x < 650 and 440 < y < 580:
        return 2,2
    return -1,-1

def main():
    global turn, bo
    player = bo.start_user
    run = True
    while run:
        if not player == "s": #show info for the players
            bo = n.send("get")
            userWindow(win, bo, player, bo.ready)
        if not player == "s":
            if bo.Game_Over("player1"):
                bo = n.send("winner player1")
            elif bo.Game_Over("player2"):
                bo = n.send("winner player2")

        if bo.winner == "player1": #print the winner
            end_screen("player1 is the Winner!")
            run = False
        elif bo.winner == "player2":
            end_screen("player2 is the winner")
            run = False
            
        for event in pygame.event.get(): #check click on exit
            if event.type == pygame.QUIT:
                if player == "player1":
                    bo = n.send("winner player2")
                else:
                    bo = n.send("winner player1")
                run = False
                quit()
                pygame.quit()

            if event.type == pygame.KEYDOWN: # q is quit the game
                if event.key == pygame.K_q and player != "s":
                    # quit game
                    if player == "player1":
                        bo = n.send("winner player2")
                    else:
                        bo = n.send("winner player1")
                        
            if event.type == pygame.MOUSEBUTTONUP and player != "s":
                if player == bo.turn and bo.ready:
                    pos = pygame.mouse.get_pos()
                    i, j = click(pos)
                    bo = n.send("select " + str(i) + " " + str(j) + " " + player)   
    n.disconnect()
    menu_screen(win)
    
#display width and height 
width = 750
height = 600
#set the display
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")
#start the game
menu_screen(win)