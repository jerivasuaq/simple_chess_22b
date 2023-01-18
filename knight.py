from piece import Piece

class Knight(Piece):
    def __init__(self, row, col, colour) -> None:
        super().__init__(row, col, colour)

    def move_to(self, row, col):
        if self.colour == 'w':
            if self.row + 1 == row:
                self.row = row
                return True
        else:
            if self.row - 1 == row:
                self.row = row
                return True

        return False

    def print(self):
        print(self.__str__())

    def __str__(self) -> str:
        if self.colour=='w':
            return '♞'
        else:
            return '♘'

    def __repr__(self):
        return self.__str__()
