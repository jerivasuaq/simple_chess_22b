from piece import Piece
from pawn import Pawn

if __name__ == '__main__':
    p = Piece(0,0,'w')
    pw = Pawn(1,1,'w')
    pw.move_to(2,1)
    pw.print()

    print("Simple Chess")
