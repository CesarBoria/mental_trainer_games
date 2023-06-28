import chess
import random


def valid_bishop_move(from_square, to_square):
    """
    Check if a bishop can move from the 'from_square' to the 'to_square' in a single diagonal move.
    Both squares should be provided in UCI notation (e.g., 'e4', 'a1', 'g8').
    Returns True if the move is valid, False otherwise.
    """
    from_square = chess.parse_square(from_square)
    to_square = chess.parse_square(to_square)

    # Get the difference in rank and file between the squares
    rank_diff = abs(chess.square_rank(to_square) - chess.square_rank(from_square))
    file_diff = abs(chess.square_file(to_square) - chess.square_file(from_square))

    # Check if the move is a valid bishop's move (diagonal)
    if rank_diff == file_diff:
        return True
    else:
        return False


def squares_same_color(square1, square2):
    """
    Check if two squares on a chessboard are of the same color.
    Returns True if the squares are of the same color, False otherwise.
    """
    return (ord(square1[0]) - ord('a') + int(square1[1])) % 2 == (ord(square2[0]) - ord('a') + int(square2[1])) % 2


def generate_random_squares():
    """
    Generate two random squares on a chessboard.
    Returns a tuple containing the two random squares in UCI notation.
    """
    random_squares = random.sample(chess.SQUARES, k=2)
    square1 = chess.square_name(random_squares[0])
    square2 = chess.square_name(random_squares[1])
    return square1, square2


def check_bishop_moves(move_list):
    """
    Check the validity of a list of bishop moves.
    Each move in the list should be a string in UCI notation.
    Prints whether each move is valid or not.
    """
    for i in range(len(move_list) - 1):
        from_square = move_list[i]
        to_square = move_list[i + 1]
        if valid_bishop_move(from_square, to_square):
            print(f"Valid bishop's move: {from_square} to {to_square}")
        else:
            print(f"Invalid bishop's move: {from_square} to {to_square}")


def compare_bishop_moves(move_list, square1, square2):
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


def play_bishop_moves_game():
    """
    Play a game where the user needs to provide a list of bishop moves.
    Random squares are generated, and the user's move list is checked for validity.
    """
    square1, square2 = generate_random_squares()
    print("Random Square 1:", square1)
    print("Random Square 2:", square2)

    can_reach_destination = input("Can the bishop reach the destination square? (yes/no): ")

    if squares_same_color(square1, square2) and can_reach_destination.lower() == "yes":
        user_input = input("Enter a list of moves starting with the first square and ending with the second square: ")
        move_list = user_input.split()
        check_bishop_moves(move_list)
        compare_bishop_moves(move_list, square1, square2)
    elif not squares_same_color(square1, square2) and can_reach_destination.lower() == "no":
        print("Correct! The bishop cannot reach the destination square.")
    else:
        print("Incorrect! The bishop can reach the destination square.")


play_bishop_moves_game()
