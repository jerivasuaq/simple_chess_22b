from piece import Piece

class Rook(Piece):
    def __init__(self, row, col, colour) -> None:
        super().__init__(row, col, colour)

    def move_to(self, row, col):
        if self.colour == 'w':
            if (self.row + 1 == row or self.row - 1 == row) and (self.col + 1 == col or self.col - 1 == col):
                self.row = row
                self.col = col
                return True

        else:
            if (self.row + 1 == row or self.row - 1 == row) and (self.col + 1 == col or self.col - 1 == col):
                self.row = row
                self.col = col
                return True

        return False

    def print(self):
        print(self.__str__())

    def __str__(self) -> str:
        if self.colour=='w':
            return '♜'
        elif self.colour=='b':
            return '♖'

    def __repr__(self):
        return self.__str__()