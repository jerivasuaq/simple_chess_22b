from piece import Piece

class Rook(Piece):
    def __init__(self, row, col, colour) -> None:
        super().__init__(row, col, colour)

    def move_to(self, row, col):
        if (self.row != row) and (self.col != col):
            return False #Error 01: Invalid movement; Try again!
        else:
            if(self.row != row):    #Vertical movement
                for i in range(abs(self.row-row)): #Gradual movement until desired position
                    temp_piece = board[i][col]
                    if (temp_piece != None) : #Is someone on the way?
                        if (temp_piece.colour== self.colour):   #Is for the same team
                            return False    #Error 02: "Shall move only %(i-1) places"
                        else:   #should be opponent
                            if(i != row):   #if cont is not yet final position, there is a piece blocking the way
                                return False    #Error 02
                            else:   #Should be at the same postition than opponent; kill him!
                                self.row= row
                                kill(temp_piece)
                                return  True
            elif (self.col != col):    #Horizontal movement
                for i in range(abs(self.col-col)): #Gradual movement until desired position
                    temp_piece = board[row][i]
                    if (temp_piece != None) : #Is someone on the way?
                        if (temp_piece.colour== self.colour):   #Is for the same team
                            return False    #Error 02: "Shall move only %(i-1) places"
                        else:   #should be opponent
                            if(i != col):   #if cont is not yet final position, there is a piece blocking the way
                                return False    #Error 02
                            else:   #Should be at the same postition than opponent; kill him!
                                self.col= col
                                kill(temp_piece)
                                return  True

    def print(self):
        print(self.__str__())

    def __str__(self) -> str:
        if self.colour=='w':
            return '♜'
        elif self.colour=='b':
            return '♖'

    def __repr__(self):
        return self.__str__()