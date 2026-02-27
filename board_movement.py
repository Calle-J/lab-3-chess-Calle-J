class BoardMovement:

    @staticmethod
    def forward(position: str, color: str, squares: int = 1):
        column = position[0]
        row = int(position[1])

        # WHITE moves "upwards" (row -)
        direction = -1 if color == "WHITE" else 1
        new_row = row + (direction * squares)

        if new_row < 1 or new_row > 8:
            return None

        return f"{column}{new_row}"

    @staticmethod
    def backward(position: str, color: str, squares: int = 1):
        column = position[0]
        row = int(position[1])

        direction = 1 if color == "WHITE" else -1
        new_row = row + (direction * squares)

        if new_row < 1 or new_row > 8:
            return None

        return f"{column}{new_row}"
    
    @staticmethod
    def left(position: str, color: str, squares: int = 1):
        column = position[0]
        row = position[1]

        new_col = chr(ord(column) - squares)

        if new_col < "a" or new_col > "h":
            return None

        return f"{new_col}{row}"

    @staticmethod
    def right(position: str, color: str, squares: int = 1):
        column = position[0]
        row = position[1]

        new_col = chr(ord(column) + squares)

        if new_col < "a" or new_col > "h":
            return None

        return f"{new_col}{row}"

    @staticmethod
    def diagonal(position: str, color: str, col_dir: int, row_dir: int, squares: int = 1):
        column = position[0]
        row = int(position[1])

        new_col = chr(ord(column) + col_dir * squares)
        new_row = row + row_dir * squares

        if new_col < "a" or new_col > "h":
            return None
        if new_row < 1 or new_row > 8:
            return None

        return f"{new_col}{new_row}"