import piece
from pawn import Pawn
class Board():
    pieces = [[0]*8]*8
    def __init__(self):
        print(self.pieces)
        for i in range(8):
            self.pieces[i][2] = Pawn(True)
        for i in range(8):
            self.pieces[i][6] = Pawn()
        self.pieces[0][0] = new Rook(True)
        self.pieces[7][0] = new Rook(True)
        self.pieces[0][7] = new Rook()
        self.pieces[7][7] = new Rook()
        self.pieces[1][0] = new Horse(True)
        self.pieces[7][0] = new Horse(True)
        self.pieces[1][7] = new Horse()
        self.pieces[7][7] = new Horse()
        self.pieces[2][0] = new Horse(True)
        self.pieces[6][0] = new Horse(True)
        
    def __str__(self):
        return self.pieces.__str__();
