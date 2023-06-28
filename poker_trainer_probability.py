import random
from pypokerengine.utils.card_utils import gen_cards, estimate_hole_card_win_rate


class ScoreTreatment:
    @staticmethod
    def calculate_score(difference):
        rewarding_points = 1 - 2 * difference
        return rewarding_points


class PokerTrainer:
    deck = ['HA', 'HK', 'HQ', 'HJ', 'HT', 'H9', 'H8', 'H7', 'H6', 'H5', 'H4', 'H3', 'H2',
            'DA', 'DK', 'DQ', 'DJ', 'DT', 'D9', 'D8', 'D7', 'D6', 'D5', 'D4', 'D3', 'D2',
            'CA', 'CK', 'CQ', 'CJ', 'CT', 'C9', 'C8', 'C7', 'C6', 'C5', 'C4', 'C3', 'C2',
            'SA', 'SK', 'SQ', 'SJ', 'ST', 'S9', 'S8', 'S7', 'S6', 'S5', 'S4', 'S3', 'S2']

    def __init__(self):
        self.score = 0

    def generate_random_scenario(self):
        # Generate random hole cards
        hole_cards = random.sample(self.deck, 2)

        # Remove hole cards from the deck
        self.deck = [card for card in self.deck if card not in hole_cards]

        # Generate random number of players (2 to 6)
        num_players = random.randint(2, 6)

        # Generate random number of community cards (0, 3, 4, or 5)
        num_community_cards = random.choice([0, 3, 4, 5])

        # Generate random community cards
        community_cards = random.sample(self.deck, num_community_cards)

        return hole_cards, num_players, community_cards

    @staticmethod
    def calculate_correct_odds(hole_cards, num_players, community_cards):
        hole_card = gen_cards(hole_cards)
        community_card = gen_cards(community_cards)
        win_rate = estimate_hole_card_win_rate(nb_simulation=10000, nb_player=num_players,
                                               hole_card=hole_card, community_card=community_card)
        return win_rate

    def play_round(self):
        # Generate a random scenario
        hole_cards, num_players, community_cards = self.generate_random_scenario()

        # Display the scenario information
        print(f"Hole Cards: {hole_cards}")
        print(f"Number of Players: {num_players}")
        print(f"Community Cards: {community_cards}")

        # Calculate the correct odds
        correct_odds = self.calculate_correct_odds(hole_cards, num_players, community_cards)

        # Prompt the user to input
        user_odds = float(input("Enter your estimated odds of winning (between 0 and 1): "))

        # Calculate the difference
        difference = abs(correct_odds - user_odds)

        # Calculate and update the score based on the difference
        self.score += ScoreTreatment.calculate_score(difference)

        # Print the user's answer, the correct response, the difference, and the score
        print(f"\nYour Answer: {user_odds}")
        print(f"Correct Response: {round(correct_odds, 2)}")
        print(f"Difference: {round(difference, 2)}")
        print(f"Score: {round(self.score, 2)}")
        print("------------------------")


# Instantiate the PokerTrainer class
trainer = PokerTrainer()

# Play the game 10 times
for _ in range(10):
    trainer.play_round()
