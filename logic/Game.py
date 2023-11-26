from logic.Player import Sam, Dealer

class Game:
    def __init__(self, deck):
        """Initialize the game with a deck of cards and two players: Sam and the Dealer."""
        self.deck = deck
        self.sam = Sam()
        self.dealer = Dealer()
        self.winner = None

    def deal_initial_cards(self):
        """Deals two cards to each player, alternating between them."""
        for _ in range(2):
            self.sam.add_card(self.deck.deal_card())
            self.dealer.add_card(self.deck.deal_card())

    def check_for_blackjack(self):
        """Checks if either player has blackjack or if both have a score of 22 with their initial hand."""
        if self.sam.hand.score == 21:
            self.winner = self.sam
        elif self.dealer.hand.score == 21 or (self.sam.hand.score == self.dealer.hand.score == 22):
            self.winner = self.dealer

    def play_sam_turn(self):
        """Allows Sam to draw cards until he decides to stop according to the rules."""
        while not self.winner and self.sam.should_draw_card():
            self.sam.add_card(self.deck.deal_card())
            if self.sam.hand.score == 21:
                self.winner = self.sam
            if self.sam.hand.score > 21:
                self.winner = self.dealer

    def play_dealer_turn(self):
        """Allows the Dealer to draw cards after Sam has finished his turn."""
        while not self.winner and self.dealer.should_draw_card(self.sam.hand.score):
            self.dealer.add_card(self.deck.deal_card())
            if self.dealer.hand.score > 21:
                self.winner = self.sam

    def determine_winner(self):
        """Determines the winner based on the scores if no one has won already."""
        if not self.winner:
            self.winner = self.sam if self.sam.hand.score > self.dealer.hand.score else self.dealer

    def play_game(self):
        """Plays a full game of blackjack according to the rules."""
        self.deal_initial_cards()
        self.check_for_blackjack()
        self.play_sam_turn()
        self.play_dealer_turn()
        self.determine_winner()

    def get_result(self) -> str:
        """Returns the result of the game with the winner and the final hands of Sam and the Dealer."""
        return f"{self.winner}\n" \
               f"sam: {self.sam}\n" \
               f"dealer: {self.dealer}"