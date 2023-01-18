from piece import Piece
#from rook import Rook #importing for class Tower

class King(Piece):
    

    def __init__(self, row, col, colour) -> None:  
        super().__init__(row, col, colour)

    
    def move_to(self, row, col):
        mov_col=0
        mov_row=0
        mov=[]
        originkb = True
        originkw = True
        originrrw = True
        originrlw = True
        originrrb = True
        originrlb = True
        check_arr = [(2,3), (1,5)]
        check = False

        if self.colour == 'w':
            if self.row == 0 and self.col == 4 and originkw == True: #checkin initial position of white king for castling
                if self.col + 2 == col and check == False and originrrw == True: #kingside castling
                    if self.col + 1 == " " and self.col + 2 == " ": #checking empty spaces
                        mov_col = col #castle
                        mov_row = row
                        originrrw = False
                elif self.col - 2 == col and check == False and originrlw == True: #queenside castling
                    if self.col + 1 == " " and self.col + 2 == " " and self.col + 3 == " ": #checking empty spaces
                        mov_col = col #castle
                        mov_row = row
                        originrlw = False
            
            if row - self.row <= 1 and col - self.col <= 1:
                mov=[row,col]
                for z in (len(check_arr)):
                    if mov not in check_arr:
                        mov_row = row
                        mov_col = col
            self.row == mov_row
            self.col == mov_col 
            originkw = False 
            return True
        else:
            if self.row == 7 and self.col == 4 and originkb == True: #checkin initial position of white king for castling
                if self.col + 2 == col and check == False and originrlb == True: #kingside castling
                    if self.col + 1 == " " and self.col + 2 == " ": #checking empty spaces
                        mov_col = col #castle
                        mov_row = row
                        originrlb = False
                elif self.col - 2 == col and check == False and originrrb == True: #queenside castling
                    if self.col + 1 == " " and self.col + 2 == " " and self.col + 3 == " ": #checking empty spaces
                        mov_col = col #castle
                        mov_row = row
                        originrrb = False
            if row - self.row <= 1 and col - self.col <= 1:
                mov=[row,col]
                for z in (len(check_arr)):
                    if mov not in check_arr[z]:
                        mov_row = row
                        mov_col = col
            self.row == mov_row
            self.col == mov_col 
            originkw = False  
            return True
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

    
