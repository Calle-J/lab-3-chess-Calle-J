from pieces import Pawn, Rook, Bishop, Knight, Queen, King
import json

class Board:
    def __init__(self):
        # Dict comprehension: Creates all squares a1-h8 with value None.

        self.squares = {
            f"{chr(col)}{row}": None
            for col in range(ord("a"), ord("i")) # a-h
            for row in range(1, 9) # 1-8
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

        white_pawns = {
            f"{file}7": Pawn("WHITE", idx)
            for idx, file in enumerate("abcdefgh", start=1)
        }
        self.squares.update(white_pawns)

        self.squares["a8"] = Rook("WHITE", 1)
        self.squares["b8"] = Knight("WHITE", 1)
        self.squares["c8"] = Bishop("WHITE", 1)
        self.squares["d8"] = Queen("WHITE", 1)
        self.squares["e8"] = King("WHITE", 1)
        self.squares["f8"] = Bishop("WHITE", 2)
        self.squares["g8"] = Knight("WHITE", 2)
        self.squares["h8"] = Rook("WHITE", 2)

        for square, piece in self.squares.items():
            if piece is not None:
                piece.set_initial_position(square)
                piece.define_board(self)

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
    
    def get_piece(self, square: str):
        # Returns the piece that is on a specific square
        return self.squares[square]
    
    def is_square_empty(self, square: str):
        # Returns True is the square is empty, False otherwise.
        return self.get_piece(square) is None
    
    def kill_piece(self, square: str):
        # Kills the piece on the given square
        piece = self.get_piece(square)
        if piece is not None:
            piece.die()
            self.squares[square] = None

    def find_piece(self, symbol: str, identifier: int, color: str):
        # Find a piece by symbol, identifier and color
        matches = [
            piece
            for square, piece in self.squares.items()
            if piece is not None
            and piece.symbol == symbol
            and piece.identifier == identifier
            and piece.color == color
        ]
        return matches[0] if matches else None
    
    def save_state(self):
        with open("board.txt", "a") as file:
            file.write(json.dumps(self.squares) + "\n")

    @staticmethod
    def load_states():
        # Generator that yields one board state (one line) at a time.
        try:
            with open("board.txt", "r") as file:
                for line in file:
                    yield line.strip()
        except FileNotFoundError:
            print("No board.txt file found.")
    
    @staticmethod
    def print_state_from_dict(state_dict):
        # Print a saved board state in the same format as print_board().
        for row in range(1, 9):
            row_pieces = []
            for col in range(ord("a"), ord("i")):
                square = f"{chr(col)}{row}"
                row_pieces.append(state_dict.get(square))
            print(row_pieces)