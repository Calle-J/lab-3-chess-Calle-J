from board import Board
import json

board = Board()
board.setup_board()

# Gör några drag så board.txt får innehåll
rook = board.find_piece("R", 1, "BLACK")
rook.move("right", 3)

pawn = board.find_piece("-", 1, "BLACK")
pawn.move()

print("\n--- Loading saved states ---")
for line in Board.load_states():
    state_dict = json.loads(line)
    Board.print_state_from_dict(state_dict)
    print("-----")