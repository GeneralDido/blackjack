import os
import sys
import unittest

# Add the parent directory to the Python path.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic.Card import Card


class TestCard(unittest.TestCase):
    def setUp(self):
        """Set up test cards."""
        self.numeric_card = Card(suit='C', value='7')
        self.face_card = Card(suit='H', value='Q')
        self.ace_card = Card(suit='S', value='A')

    def test_card_score_numeric(self):
        self.assertEqual(self.numeric_card.score, 7)

    def test_card_score_face(self):
        self.assertEqual(self.face_card.score, 10)

    def test_card_score_ace_high(self):
        self.assertEqual(self.ace_card.score, 11)
        

if __name__ == '__main__':
    unittest.main()