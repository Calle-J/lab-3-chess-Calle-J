from abc import ABC, abstractmethod
from board_movement import BoardMovement
import functools

#------------------------
#
#       DECORATORS
#
#------------------------

def print_board_after_move(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        if self.board:
            print("\nBoard after move:")
            self.board.print_board()
        return result
    return wrapper

def save_board_after_move(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        if self.board:
            self.board.save_state()
        return result
    return wrapper

#------------------------
#
#       BASE CLASS
#
#------------------------

class BaseChessPiece(ABC, dict):
    def __init__(self, color: str, identifier: int, name: str, symbol: str):
        self.color = color
        self.identifier = identifier
        self.name = name
        self.symbol = symbol
        self.position = None
        self.is_alive = True
        self.board = None

        dict.__init__(self, 
                      color=color, 
                      identifier=identifier, 
                      name=name, symbol=symbol, 
                      position=None, 
                      is_alice=True)

    @abstractmethod
    def move(self, *args, **kwargs):
        # Each piece must implement its own logic.
        pass

    def die(self):
        # Toggle is_alive to Flase.
        self.is_alive = False
    
    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"
    
    def __repr__(self):
        return self.__str__()
    
    def base_move(self, movement: str):
        print(movement)

    def set_initial_position(self, position):
        self.position = position
        self["position"] = position
    
    def define_board(self, board):
        self.board = board

    @save_board_after_move
    @print_board_after_move
    def apply_movement(self, new_square: str):
        if new_square is None:
            print("Invalid move: outside board")
            return
        
        target_piece = self.board.get_piece(new_square)

        if target_piece is not None:
            if target_piece.color == self.color:
                print("Blocked by fiendly piece")
                return
            else:
                target_piece.die()
        
        self.board.squares[self.position] = None
        self.position = new_square
        self["position"] = new_square
        self.board.squares[self.position] = self
    
#---------------------------
#
#       PIECE CLASSES
#
#---------------------------

class Pawn(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier, "Pawn", "-")
    
    def move(self):
        new_square = BoardMovement.forward(self.position, self.color, 1)
        self.apply_movement(new_square)

class Rook(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier, "Rook", "R")

    def move(self, direction: str, squares: int):
        if direction == "left":
            new_square = BoardMovement.left(self.position, squares)
        elif direction == "right":
            new_square = BoardMovement.right(self.position, squares)
        elif direction == "forward":
            new_square = BoardMovement.forward(self.position, self.color, squares)
        elif direction == "backward":
            new_square = BoardMovement.backward(self.position, self.color, squares)
        else:
            print("Invalid direction")
            return
        self.apply_movement(new_square)

class Bishop(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier, "Bishop", "B")

    def move(self, col_dir: int, row_dir: int, squares: int):
        new_square = BoardMovement.diagonal(self.position, col_dir, row_dir, squares)
        self.apply_movement(new_square)

class Knight(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier, "Knight", "N")

    def move(self, col_change: int, row_change: int):
        new_col = chr(ord(self.position[0]) + col_change)
        new_row = int(self.position[1]) + row_change

        if new_col < "a" or new_col > "h" or new_row < 1 or new_row > 8:
            print("Knight cannot move outside board")
            return

        new_square = f"{new_col}{new_row}"
        self.apply_movement(new_square)

class Queen(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier, "Queen", "Q")
    
    def move(self, col_dir: int, row_dir: int, squares: int):
        new_square = BoardMovement.diagonal(self.position, col_dir, row_dir, squares)
        self.apply_movement(new_square)

class King(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier, "King", "K")

    def move(self, col_dir: int, row_dir: int):
        new_square = BoardMovement.diagonal(self.position, col_dir, row_dir, 1)
        self.apply_movement(new_square)