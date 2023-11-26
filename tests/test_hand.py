import unittest

import os
import sys

# Add the parent directory to the Python path.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic.Card import Card
from logic.Hand import Hand


class TestHand(unittest.TestCase):
    def setUp(self):
        """Set up a hand for testing."""
        self.hand = Hand()

    def test_hand_add_card(self):
        card = Card(suit='C', value='7')
        self.hand.add_card(card)
        self.assertIn(card, self.hand.cards)

    def test_hand_score(self):
        self.hand.add_card(Card(suit='C', value='7'))
        self.hand.add_card(Card(suit='H', value='Q'))
        self.assertEqual(self.hand.score, 17)

    def test_hand_score_with_ace(self):
        self.hand.add_card(Card(suit='C', value='A'))
        self.hand.add_card(Card(suit='H', value='Q'))
        self.assertEqual(self.hand.score, 21)


if __name__ == '__main__':
    unittest.main()