import pygame,os
cross = pygame.image.load(os.path.join("img", "x.png"))
circle = pygame.image.load(os.path.join("img", "y.png"))

class Board:
    rect = (100, 100, 500, 500)
    startX = rect[0]
    startY = rect[1]
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.ready = False
        self.board = [[0,0,0] for _ in range(rows)]
        self.p1Name = "player1"
        self.p2Name = "player2"
        self.turn = "player1"
        self.winner = None
    
    def select(self,col, row, player): #select on the board
        if -1<row<3 and -1<col<3:
            if self.board[row][col] == 0: 
                if player == self.p1Name:
                    self.board[row][col] = 1 # 1 = cross
                    self.turn = self.p2Name
                if player == self.p2Name:
                    self.board[row][col] = 2 # 2 = circle  
                    self.turn = self.p1Name
                    
    def draw(self, win): #print the cross and circle on the display
        if self.board[0][0] == 1:
            win.blit(cross,(125,50))
        if self.board[0][0] == 2:
            win.blit(circle,(125,50))
        if self.board[0][1] == 1:
            win.blit(cross,(125,240))
        if self.board[0][1] == 2:
            win.blit(circle,(125,240))
        if self.board[0][2] == 1:
            win.blit(cross,(125,440))
        if self.board[0][2] == 2:
            win.blit(circle,(125,440))
            
        if self.board[1][0] == 1:
            win.blit(cross,(310,50))
        if self.board[1][0] == 2:
            win.blit(circle,(310,50))   
        if self.board[1][1] == 1:
            win.blit(cross,(310,240))
        if self.board[1][1] == 2:
            win.blit(circle,(310,240))
        if self.board[1][2] == 1:
            win.blit(cross,(310,440))
        if self.board[1][2] == 2:
            win.blit(circle,(310,440))
            
        if self.board[2][0] == 1:
            win.blit(cross,(480,50))
        if self.board[2][0] == 2:
            win.blit(circle,(480,50))
        if self.board[2][1] == 1:
            win.blit(cross,(480,240))
        if self.board[2][1] == 2:
            win.blit(circle,(480,240))
        if self.board[2][2] == 1:
            win.blit(cross,(500,460))
        if self.board[2][2] == 2:
            win.blit(circle,(500,460))

    def Game_Over(self, player): #check if someone win
        #row
        if self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][2]:
            if self.board[0][0] != 0 and self.board[0][1] != 0 and self.board[0][2] !=0 and player!=self.turn:
                return True
        if self.board[1][0] == self.board[1][1] and self.board[1][1] == self.board[1][2]:
            if self.board[1][0] != 0 and self.board[1][1] != 0 and self.board[1][2] !=0 and player!=self.turn:
                return True
        if self.board[2][0] == self.board[2][1] and self.board[2][1] == self.board[2][2]:
            if self.board[2][0] != 0 and self.board[2][1] != 0 and self.board[2][2] !=0 and player!=self.turn:
                return True
        #col
        if self.board[0][0] == self.board[1][0] and self.board[1][0] == self.board[2][0]:
            if self.board[0][0] != 0 and self.board[1][0] != 0 and self.board[2][0] !=0 and player!=self.turn:
                return True
        if self.board[0][1] == self.board[1][1] and self.board[1][1] == self.board[2][1]:
            if self.board[0][1] != 0 and self.board[1][1] != 0 and self.board[2][1] !=0 and player!=self.turn:
                return True
        if self.board[0][2] == self.board[1][2] and self.board[1][2] == self.board[2][2]:
            if self.board[0][2] != 0 and self.board[1][2] != 0 and self.board[2][2] !=0 and player!=self.turn:
                return True
        #diagnol
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            if self.board[0][0] != 0 and self.board[1][1] != 0 and self.board[2][2] !=0 and player!=self.turn:
                return True
        if self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2]:
            if self.board[2][0] != 0 and self.board[1][1] != 0 and self.board[0][2] !=0 and player!=self.turn:
                return True
        return False
