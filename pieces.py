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
    
    def base_move(self, movement: str):
        print(movement)
    
#---------------------------
#
#       PIECE CLASSES
#
#---------------------------

class Pawn(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier, "Pawn", "-")
    
    def move(self):
        movement = "Pawn moves forward 1 position"
        super().baseMove(movement)

class Rook(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier, "Rook", "R")

    def move(self):
        movement = "Rook moves horizontally or vertically"
        super().baseMove(movement)

class Bishop(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier, "Bishop", "B")

    def move(self):
        movement = "Bishop moves diagonally"
        super().baseMove(movement)

class Knight(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier, "Knight", "N")

    def move(self):
        movement = "Knight moves in an L-shape"
        super().baseMove(movement)

class Queen(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier, "Queen", "Q")
    
    def move(self):
        movement = "Queen moves in all directions"
        super().baseMove(movement)

class King(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier, "King", "K")

    def move(self):
        movement = "King moves 1 square in any direction"
        super().baseMove(movement)