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


        black_pawns = {
            f"{file}2": Pawn("BLACK", idx)
            for idx, file in enumerate("abcdefgh", start=1)
        }
        self.squares.update(black_pawns)

        white_pawms = {
            f"{file}7": Pawn("WHITE", idx)
            for idx, file in enumerate("abcdefgh", start=1)
        }
        self.squares.update(white_pawms)

        self.squares["a8"] = Rook("WHITE", 1)
        self.squares["b8"] = Knight("WHITE", 1)
        self.squares["c8"] = Bishop("WHITE", 1)
        self.squares["d8"] = Queen("WHITE", 1)
        self.squares["e8"] = King("WHITE", 1)
        self.squares["f8"] = Bishop("WHITE", 2)
        self.squares["g8"] = Knight("WHITE", 2)
        self.squares["h8"] = Rook("WHITE", 2)

    def print_board(self):
        rows = []
        for row in range(1, 9):
            row_pieces = []
            for col in range(ord("a"), ord("i")):
                square = f"{chr(col)}{row}"
                row_pieces.append(self.squares[square])
            rows.append(row_pieces)
        
        for row in rows:
            print(row)