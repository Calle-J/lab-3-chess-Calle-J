from pieces import Pawn, Rook, Bishop, Knight, Queen, King

class Board:
    def __init__(self):
        # Dict comprehension: Creates all squares a1-h8 with value None.

        self.squares = {
            f"{chr(col)}{row}": None
            for col in range(ord("a"), ord("i"))
            for row in range(1, 9)
        }
    
    def setup_board(self):
        self.squares["a1"] = Rook("BLACK", 1)
        self.squares["b1"] = Knight("BLACK", 1)
        self.squares["c1"] = Bishop("BLACK", 1)
        self.squares["d1"] = Queen("BLACK", 1)
        self.squares["e1"] = King("BLACK", 1)
        self.squares["f1"] = Bishop("BLACK", 2)
        self.squares["g1"] = Knight("BLACK", 2)
        self.squares["h1"] = Rook("BLACK", 2)
        