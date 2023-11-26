from abc import ABC, abstractmethod
from logic.Hand import Hand
from logic.Card import Card


class Player(ABC):
    def __init__(self):
        self.hand = Hand()

    def add_card(self, card: Card):
        """Add a card to the player's hand."""
        self.hand.add_card(card)

    @abstractmethod
    def should_draw_card(self) -> bool:
        """Determine if the player should draw a card. This must be implemented by subclasses."""
        pass

    def __str__(self):
        """String representation of the player's hand."""
        return str(self.hand)


class Sam(Player):
    def should_draw_card(self) -> bool:
        # Sam must stop drawing cards from the deck if their total reaches 17 or higher.
        return self.hand.score < 17


class Dealer(Player):
    def should_draw_card(self, opponent_score: int) -> bool:
        # The dealer must stop drawing cards when their total is higher than Sam.
        return self.hand.score <= opponent_score
