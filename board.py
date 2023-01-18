from pawn import Pawn
from rook import Rook

class Board():
    board = []

    def __init__(self) -> None:
        txt_board = [
            "RHBQKBHR",
            "PPPPPPPP",
            "        ",
            "        ",
            "        ",
            "        ",
            "pppppppp",
            "rhbkqbhr",
        ]

        self.board = []
        for row in range(8):
            self.board.append([None]*8) 

        for row in range(8):
            for col in range(8):
                c = txt_board[row][col]
                if c == 'p':
                    self.board[row][col]= Pawn(row,col,'w')
                if c == 'P':
                    self.board[row][col]= Pawn(row,col,'b')
                if c == 'r':
                    self.board[row][col]= Rook(row,col,'w')
                if c == 'R':
                    self.board[row][col]= Rook(row,col,'b')

    def __str__(self) -> str:
        s = ''
        for row in range(8):
            for col in range(8):
                if self.board[row][col] is None:
                    s+=' '
                else:
                    s+= str(self.board[row][col])
            s+='\n'

        return s
