import unittest
import tempfile
import os
import sys
from unittest.mock import patch
from io import StringIO

# Add the parent directory to the Python path.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic.Card import Card
from logic.Deck import Deck
from logic.GameIO import GameIO
from logic.Player import Sam, Dealer


class TestGameIO(unittest.TestCase):
    def setUp(self):
        """Set up a temporary file and players for testing."""
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.write(b"CA, D5, H9, HQ, S8")
        self.temp_file.close()

        self.sam = Sam()
        self.dealer = Dealer()

    def tearDown(self):
        """Clean up the temporary file after testing."""
        os.unlink(self.temp_file.name)

    def test_read_deck_from_file(self):
        deck = GameIO.read_deck_from_file(self.temp_file.name)
        self.assertIsInstance(deck, Deck)
        self.assertEqual(len(deck.cards), 5)
        
    def test_output_game_results(self):
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            GameIO.output_game_results(self.sam, self.sam, self.dealer)
        output = fake_stdout.getvalue().strip()
        self.assertEqual(output, "sam\nsam: \ndealer:")
        

if __name__ == '__main__':
    unittest.main()
