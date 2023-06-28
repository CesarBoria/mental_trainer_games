import chess
import random


def valid_knight_move(from_square, to_square):
    """
    Check if a knight can move from the 'from_square' to the 'to_square' in a single jump.
    Both squares should be provided in UCI notation (e.g., 'e4', 'a1', 'g8').
    Returns True if the move is valid, False otherwise.
    """
    from_square = chess.parse_square(from_square)
    to_square = chess.parse_square(to_square)

    # Get the difference in rank and file between the squares
    rank_diff = abs(chess.square_rank(to_square) - chess.square_rank(from_square))
    file_diff = abs(chess.square_file(to_square) - chess.square_file(from_square))

    # Check if the move is a valid knight's move
    if (rank_diff == 1 and file_diff == 2) or (rank_diff == 2 and file_diff == 1):
        return True
    else:
        return False


def generate_random_squares():
    """
    Generate two random squares on a chessboard.
    Returns a tuple containing the two random squares in UCI notation.
    """
    random_squares = random.sample(chess.SQUARES, k=2)
    square1 = chess.square_name(random_squares[0])
    square2 = chess.square_name(random_squares[1])
    return square1, square2


def check_knight_moves(move_list):
    """
    Check the validity of a list of knight moves.
    Each move in the list should be a string in UCI notation.
    Prints whether each move is valid or not.
    """
    for i in range(len(move_list) - 1):
        from_square = move_list[i]
        to_square = move_list[i + 1]
        if valid_knight_move(from_square, to_square):
            print(f"Valid knight's move: {from_square} to {to_square}")
        else:
            print(f"Invalid knight's move: {from_square} to {to_square}")


def compare_knight_moves(move_list, square1, square2):
    """
    Compare the first and last squares of a list of UCI moves to two given squares.
    The move_list should be a list of UCI moves.
    The square1 and square2 parameters should be the squares to compare against.
    Prints whether the first and last squares match the given squares or not.
    """
    first_square = move_list[0]
    last_square = move_list[-1]

    if first_square == square1 and last_square == square2:
        print("First and last squares match the given squares.")
    else:
        print("First and last squares do not match the given squares.")


def play_knight_moves_game():
    # Step 1: Print two random squares
    square1, square2 = generate_random_squares()
    print("Random Square 1:", square1)
    print("Random Square 2:", square2)

    # Step 2: Request user input for the list of moves
    user_input = input("Enter a list of moves starting with the first square and ending with the second square: ")
    move_list = user_input.split()

    # Step 3: Check if each pair of moves is a valid knight move
    check_knight_moves(move_list)

    # Step 4: Inform the user about the correctness of their move list
    compare_knight_moves(move_list, square1, square2)


# Play the knight moves game
play_knight_moves_game()
