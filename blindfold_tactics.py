import requests
import chess.pgn

# Replace 'TACTIC_ID' with the actual ID of the tactic you want to retrieve
tactic_id = '0MIcZ'

# Make a GET request to the Lichess API to fetch the tactic data
response = requests.get(f'https://lichess.org/api/puzzle/{tactic_id}')

# Check if the request was successful
if response.status_code == 200:
    tactic_data = response.json()

    # Print the FEN notation
    print(f"FEN Notation: {tactic_data}")
    FEN = tactic_data['game']['pgn']
    print(f"FEN Notation: {FEN}")

else:
    print(f"Error: Failed to fetch tactic data. Status Code: {response.status_code}")


