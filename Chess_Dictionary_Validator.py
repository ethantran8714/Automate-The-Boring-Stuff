"""
In this chapter, we used the dictionary value
{'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board.

Write a function named isValidChessBoard() that takes a dictionary argument
and returns True or False depending on if the board is valid.

A valid board will have exactly one black king and exactly one white king.
Each player can only have at most 16 pieces, at most 8 pawns,
and all pieces must be on a valid space from '1a' to '8h';
that is, a piece can’t be on space '9z'.

The piece names begin with either a 'w' or 'b' to represent white or black,
followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.

This function should detect when a bug has resulted in an improper chess board.


"""


def is_valid_chess_board(board):
    valid_spaces = ["1a", "1b", "1c", "1d", "1e", "1f", "1g", "1h",
                    "2a", "2b", "2c", "2d", "2e", "2f", "2g", "2h",
                    "3a", "3b", "3c", "3d", "3e", "3f", "3g", "3h",
                    "4a", "4b", "4c", "4d", "4e", "4f", "4g", "4h",
                    "5a", "5b", "5c", "5d", "5e", "5f", "5g", "5h",
                    "6a", "6b", "6c", "6d", "6e", "6f", "6g", "6h",
                    "6a", "6b", "6c", "6d", "6e", "6f", "6g", "6h",
                    "6a", "6b", "6c", "6d", "6e", "6f", "6g", "6h"]

    black_valid_pieces = ['bpawn', 'bknight', 'bbishop', 'brook', 'bqueen', 'bking', "", " "]
    white_valid_pieces = ['wpawn', 'wknight', 'wbishop', 'wrook', 'wqueen', 'wking', "", " "]
    board_values = list(board.values())
    board_keys = list(board.keys())
    black_king = board_values.count("bking")
    white_king = board_values.count("wking")
    black_pawn_numbers = board_values.count("bpawn")
    white_pawn_numbers = board_values.count("wpawn")
    total_black = 0
    total_white = 0

    # sums up number of pieces on both sides
    for piece in board_values:
        if piece in black_valid_pieces:
            total_black += 1
        elif piece in white_valid_pieces:
            total_white += 1
        else:
            return False

    # checks validity of 1 white king, 1 black king, player pieces of 16 or less,
    # checks if pawns are at most 8 for both players
    if total_black <= 16 and total_white <= 16 and black_king == 1 and white_king == 1 and black_pawn_numbers <= 8 and white_pawn_numbers <= 8:
        # checks validity of space
        for space in board_keys:
            if space in valid_spaces:
                pass
            else:
                return False
        # check validity of pieces
        for key in board_values:
            if key in white_valid_pieces or key in black_valid_pieces:
                pass
            else:
                return False
    return True


print(is_valid_chess_board({'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}))
