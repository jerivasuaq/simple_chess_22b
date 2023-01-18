from piece import Piece
from tower import Tower

class King(Piece, Tower):
    originkw=False
    originkb=False

    def __init__(self, row, col, colour, check) -> None: #añadir check a la clase Piece
        super().__init__(row, col, colour, check)


    def move_to(self, row, col):

        if self.colour == 'w':
            if self.row == 0 and self.col == 4: #comprobando posición inicial del rey blanco
                originkw=True
            if originkw == True and self.row + 2 == row and self.check == False:
                if origintw == True:
                    self.row


            if self.row + 1 == row:
                self.row = row
                return True
        else:
            if self.row == 7 and self.col == 4: #comprobando posición inicial del rey negro
                originkb=True

            if self.row - 1 == row:
                self.row = row
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

    
