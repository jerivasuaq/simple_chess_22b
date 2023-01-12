class Piece:
    colour = "black"
    row = -1
    col = -1

    def __init__(self, row, col, colour) -> None:
        self.row = row
        self.col = col
        self.colour = colour

    def move_to(self, row, col):
        pass

    def print(self):
        pass

if __name__ == '__main__':
    print("Simple Chess")
