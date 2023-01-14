from piece import Piece
from pawn import Pawn

if __name__ == '__main__':
    p = Piece(0,0,'w')
    pw = Pawn(1,1,'w')
    pw.move_to(2,1)
    pw.print()

    txt_board = [
        "        ",
        "PPPPPPPP",
        "        ",
        "        ",
        "        ",
        "        ",
        "        ",
        "pppppppp",
        "        ",
    ]

    board = []
    for row in range(8):
        board.append([None]*8) 

    for row in range(8):
        for col in range(8):
            c = txt_board[row][col]
    range(8):
            if board[row][col] is None:
                print(' ',end='')
            else:
                print(board[row][col],end='')
        print()

    print("🏁🏁🏁")
