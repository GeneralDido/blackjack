import random
from collections import deque
from logic.Card import Card
from .constants import SUITS, VALUES

class Deck:
    """Represents a deck of playing cards."""
    def __init__(self, cards=None):
        """Initializes the deck with a standard set of 52 playing cards and shuffles them."""
        if cards is None:
            self.cards = deque(self.create_standard_deck())
            self.shuffle()
        else:
            self.cards = deque(cards)

    @staticmethod
    def create_standard_deck() -> list[Card]:
        """Creates a standard 52-card deck."""
        return [Card(suit, value) for suit in SUITS for value in VALUES]

    def shuffle(self):
        """Shuffles the deck of cards randomly."""
        random.shuffle(self.cards)

    def deal_card(self) -> Card:
        """Deals (removes and returns) the top card from the deck. Raises an error if the deck is empty."""
        if not self.cards:
            raise ValueError("No more cards to deal.")
        return self.cards.popleft()
