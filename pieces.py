from abc import ABC, abstractmethod

class BaseChessPiece(ABC):
    def __init__(self, color: str, identifier: int, name: str, symbol: str):
        self.color = color
        self.identifier = identifier
        self.name = name
        self.symbol = symbol
        self.position = None
        self.is_alive = True

    @abstractmethod
    def move(self):
        # Each piece must implement its own logic.
        pass

    def die(self):
        # Toggle is_alive to Flase.
        self.is_alive = False
    
    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"
    
    def __repr__(self):
        return self.__str__()
    
#---------------------------
#
#       PIECE CLASSES
#
#---------------------------

class Pawn(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier, "Pawn", "-")
    
    def move(self):
        print("Pawn moves forward 1 position")

class Rook(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier, "Rook", "R")

    def move(self):
        print("Rook moves horizontally or vertically")

class Bishop(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier, "Bishop", "B")

    def move(self):
        print("Bishop moves diagonally")

class Knight(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier, "Knight", "N")

    def move(self):
        print("Knight moves in an L-shape")

class Queen(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier, "Queen", "Q")
    
    def move(self):
        print("Queen moves in all directions")

class King(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier, "King", "K")

    def move(self):
        print("King moves 1 square in any direction")