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