import os
import sys
import unittest

# Add the parent directory to the Python path.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic.Card import Card
from logic.Deck import Deck
from logic.Game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        """Set up a game for testing."""
        self.deck = Deck()
        self.game = Game(self.deck)

    def test_initial_blackjack_dealer_wins(self):
        # Create a deck where the Dealer would get blackjack immediately.
        cards = [Card('H', '8'), Card('S', 'A'), Card('H', '7'), Card('S', 'K')]
        self.game.deck = Deck(cards)
        self.game.play_game()
        # Check if Dealer is the winner
        self.assertEqual(self.game.winner, self.game.dealer)

    def test_both_players_start_with_22_dealer_wins(self):
        # Create a deck where both players start with Aces.
        cards = [Card('S', 'A'), Card('H', 'A'), Card('D', 'A'), Card('C', 'A')]
        self.game.deck = Deck(cards)
        self.game.play_game()
        # Check if Dealer is the winner
        self.assertEqual(self.game.winner, self.game.dealer)

    def test_sam_stops_at_seventeen(self):
        # Sam should stop drawing cards when his score is 17 or more
        cards = [Card('C', '5'), Card('H', '9'), Card('C', '6'), Card('H', '7'), Card('S', '6'), Card('S', '2')]
        self.game.deck = Deck(cards)
        self.game.play_game()
        # Sam's score should be 17 and he should have drawn the third card ('S', '6')
        self.assertEqual(self.game.sam.hand.score, 17)
        self.assertIn(Card('S', '6'), self.game.sam.hand.cards)
        
    def test_dealer_draws_until_winning(self):
        # Dealer should continue drawing cards until the score is higher than Sam's
        cards = [Card('C', '10'), Card('H', '10'), Card('C', '6'), Card('H', '5'), Card('S', '3'), Card('S', '2'), Card('S', '4')]
        deck = Deck(cards)
        game = Game(deck)
        game.play_game()
        # Dealer's score should be higher than Sam's but not over 21
        self.assertTrue(game.dealer.hand.score > game.sam.hand.score and game.dealer.hand.score <= 21)

    def test_sam_busts_dealer_wins(self):
        # If Sam busts by going over 21, the dealer wins
        cards = [Card('C', '10'), Card('H', '8'), Card('C', '5'), Card('H', '9'), Card('S', '9')]
        deck = Deck(cards)
        game = Game(deck)
        game.play_game()
        # Sam should have a score over 21 and the dealer should win
        self.assertTrue(game.sam.hand.score > 21)
        self.assertEqual(game.winner, game.dealer)

    def test_dealer_busts_sam_wins(self):
        # If Dealer busts by going over 21, Sam wins
        cards = [Card('C', '10'), Card('H', '10'), Card('C', '8'), Card('H', '7'), Card('S', '6')]
        deck = Deck(cards)
        game = Game(deck)
        game.play_game()
        # Dealer should have a score over 21 and Sam should win
        self.assertTrue(game.dealer.hand.score > 21)
        self.assertEqual(game.winner, game.sam)
        
    def test_sam_gets_blackjack(self):
        # Sam gets a blackjack in the initial deal
        cards = [Card('S', 'A'), Card('H', '10'), Card('C', '10'), Card('D', '10')]
        deck = Deck(cards)
        game = Game(deck)
        game.play_game()
        # Sam should be the winner
        self.assertEqual(game.winner, game.sam)

    def test_dealer_gets_blackjack(self):
        # Dealer gets a blackjack in the initial deal
        cards = [Card('S', '10'), Card('H', 'A'), Card('C', '10'), Card('D', '10')]
        deck = Deck(cards)
        game = Game(deck)
        game.play_game()
        # Dealer should be the winner
        self.assertEqual(game.winner, game.dealer)

    def test_both_get_blackjack(self):
        # Both players get a blackjack in the initial deal
        cards = [Card('S', 'A'), Card('H', 'A'), Card('C', '10'), Card('D', '10')]
        deck = Deck(cards)
        game = Game(deck)
        game.play_game()
        # Sam should be the winner
        self.assertEqual(game.winner, game.sam)

    def test_sam_and_dealer_bust(self):
        # Sam stops and the dealer busts
        cards = [Card('S', '10'), Card('H', '10'), Card('C', '10'), Card('D', '10'), Card('S', '2'), Card('H', '2')]
        deck = Deck(cards)
        game = Game(deck)
        game.play_game()
        # Sam should be the winner
        self.assertEqual(game.winner, game.sam)


if __name__ == '__main__':
    unittest.main()