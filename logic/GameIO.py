import os
from logic.Deck import Deck
from logic.Card import Card
from logic.Player import Player, Sam, Dealer


class GameIO:
    @staticmethod
    def read_deck_from_file(file_path: str) -> Deck:
        """Reads a deck of cards from a given file and returns a Deck object."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        with open(file_path, 'r') as file:
            card_strings = file.read().strip().split(', ')
            cards = [Card(suit=card_str[0], value=card_str[1:]) for card_str in card_strings]
            return Deck(cards)

    @staticmethod
    def output_game_results(winner: Player, sam: Sam, dealer: Dealer):
        """Prints the results of the game in the specified format."""
        winner_name = 'sam' if winner == sam else 'dealer'
        print(f"{winner_name}\nsam: {sam}\ndealer: {dealer}")
