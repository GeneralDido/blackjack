import os
import sys
import unittest

# Add the parent directory to the Python path.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic.Card import Card
from logic.Deck import Deck
from logic.Hand import Hand
from logic.Player import Sam, Dealer


class TestPlayer(unittest.TestCase):
    def setUp(self):
        """Set up a player for testing."""
        self.player = Sam()  # Sam class for testing, but any Player type would do.

    def test_player_initialization(self):
        self.assertIsInstance(self.player.hand, Hand, "Player should initialize with a Hand instance.")


class TestSam(unittest.TestCase):
    def setUp(self):
        """Set up a Sam player for testing."""
        self.sam = Sam()

    def test_sam_should_draw_card(self):
        self.sam.add_card(Card(suit='C', value='5'))
        self.sam.add_card(Card(suit='H', value='10'))
        # Sam's score is 15, should draw another card
        self.assertTrue(self.sam.should_draw_card())

    def test_sam_should_not_draw_card(self):
        self.sam.add_card(Card(suit='C', value='10'))
        self.sam.add_card(Card(suit='H', value='7'))
        # Sam's score is 17, should not draw another card
        self.assertFalse(self.sam.should_draw_card())


class TestDealer(unittest.TestCase):
    def test_dealer_should_draw_card(self):
        dealer = Dealer()
        dealer.add_card(Card(suit='C', value='10'))
        dealer.add_card(Card(suit='H', value='2'))
        # Dealer's score is 12, opponent's score is 15, should draw another card
        self.assertTrue(dealer.should_draw_card(opponent_score=15))

    def test_dealer_should_not_draw_card(self):
        dealer = Dealer()
        dealer.add_card(Card(suit='C', value='10'))
        dealer.add_card(Card(suit='H', value='7'))
        # Dealer's score is 17, opponent's score is 16, should not draw another card
        self.assertFalse(dealer.should_draw_card(opponent_score=16))


if __name__ == '__main__':
    unittest.main()