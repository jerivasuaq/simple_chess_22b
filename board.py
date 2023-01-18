from pawn import Pawn
from king import King

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
            "rhbqkbhr",
        ]

        self.board = []
        for row in range(8):
            self.board.append([None]*8) 

        for row in range(8):
            for col in range(8):
                c = txt_board[row][col]
                if c == 'p':
                    self.board[row][col]= Pawn(row,col,'w')
                elif c == 'P':
                    self.board[row][col]= Pawn(row,col,'b')
                elif c == 'k':
                    self.board[row][col]= King(row,col,'w')
                elif c == 'K':
                    self.board[row][col]= King(row,col,'b')

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
