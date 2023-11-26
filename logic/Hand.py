from logic.Card import Card

class Hand:
    def __init__(self):
        """Initializes a hand for a player, starting with no cards."""
        self.cards = []

    def add_card(self, card: Card):
        """Adds a card to the player's hand."""
        self.cards.append(card)

    @property
    def score(self) -> int:
        """Calculates and returns the score for the hand, always counting Aces as 11."""
        score = sum(card.score for card in self.cards)
        return score

    def __str__(self):
        """Returns a string representation of the hand, showing all the cards it contains."""
        return ', '.join(str(card) for card in self.cards)

