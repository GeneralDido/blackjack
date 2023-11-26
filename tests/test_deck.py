import os
import sys
import unittest
import copy

# Add the parent directory to the Python path.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic.Card import Card
from logic.Deck import Deck


class TestDeck(unittest.TestCase):
    def setUp(self):
        """Set up a deck for testing."""
        self.deck = Deck()

    def test_deck_length(self):
        self.assertEqual(len(self.deck.cards), 52)

    def test_deck_deal_card(self):
        dealt_card = self.deck.deal_card()
        self.assertIsInstance(dealt_card, Card)
        self.assertEqual(len(self.deck.cards), 51)

    def test_deck_shuffle(self):
        deck_copy = copy.deepcopy(self.deck)
        self.deck.shuffle()
        self.assertNotEqual(self.deck.cards, deck_copy.cards, "It's unlikely (but not impossible) that a shuffle results in the same order")

if __name__ == '__main__':
    unittest.main()