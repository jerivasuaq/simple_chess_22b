from piece import Piece
from tower import Tower #importing for class Tower

class King(Piece, Tower):
    

    def __init__(self, row, col, colour, check, check_arr) -> None: #add check and check_arr to class Piece 
        super().__init__(row, col, colour, check, check_arr)

    
    def move_to(self, row, col):
        mov_col=0
        mov_row=0
        mov=[]
    #     check_aux=[]
    #     ch if self.row != 0 and self.row != 7 and self.col != 0 and self.col != 7:
    #         for x in eck_status=False
    #    range(self.row - 1, self.row + 1):
    #             self.row=x
    #             if self.row
    #             for y in range(self.col - 1, self.col + 1):
                    
    #                 self.col=y
        if self.colour == 'w':
            if self.row == 0 and self.col == 4: #checkin initial position of white king for castling
                if self.col + 2 == col and self.check == False and origintrw == True: #kingside castling
                    if self.col + 1 == " " and self.col + 2 == " ": #checking empty spaces
                        mov_col = col #castle
                elif self.col - 2 == col and self.check == False and origintlw == True: #queenside castling
                    if self.col + 1 == " " and self.col + 2 == " " and self.col + 3 == " ": #checking empty spaces
                        mov_col = col #castle
            
            if row - self.row <= 1 and col - self.col <= 1:
                mov=[row,col]
                for z in (len(check_arr)):
                    if mov not in check_arr:
                        mov_row = row
                        mov_col = col
            
            self.row == mov_row
            self.col == mov_col    
                
        else:
            if self.row == 7 and self.col == 4: #checkin initial position of white king for castling
                if self.col + 2 == col and self.check == False and origintrw == True: #kingside castling
                    if self.col + 1 == " " and self.col + 2 == " ": #checking empty spaces
                        mov_col = col #castle
                elif self.col - 2 == col and self.check == False and origintlw == True: #queenside castling
                    if self.col + 1 == " " and self.col + 2 == " " and self.col + 3 == " ": #checking empty spaces
                        mov_col = col #castle
            
            if row - self.row <= 1 and col - self.col <= 1:
                mov=[row,col]
                for z in (len(check_arr)):
                    if mov not in check_arr:
                        mov_row = row
                        mov_col = col
            
            self.row == mov_row
            self.col == mov_col 

        return False

    def print(self):
        print(self.__str__())

    def __str__(self) -> str:
        if self.colour=='w':
            return '♚'
        else:
            return '♔'

    def __repr__(self):
        return self.__str__()

    
