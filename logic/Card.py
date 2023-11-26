from dataclasses import dataclass
from .constants import SUITS, VALUES

@dataclass
class Card:
    suit: str
    value: str

    VALID_SUITS = set(SUITS)
    VALID_VALUES = set(VALUES)
    SCORES = {str(i): i for i in range(2, 11)}
    SCORES.update({'J': 10, 'Q': 10, 'K': 10, 'A': 11})

    def __post_init__(self):
        """Validates the suit and value of the card upon initialization."""
        if self.suit not in self.VALID_SUITS:
            raise ValueError(f"Invalid suit: {self.suit}")
        if self.value not in self.VALID_VALUES:
            raise ValueError(f"Invalid value: {self.value}")

    @property
    def score(self) -> int:
        return self.SCORES[self.value]

    def __str__(self):
        """
        Returns a string representation of the card, combining its value and suit.
        """
        return f"{self.suit}{self.value}"