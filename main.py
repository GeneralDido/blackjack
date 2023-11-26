import sys
from logic.GameIO import GameIO
from logic.Deck import Deck
from logic.Game import Game

def main():
    deck = None

    # Check if a file path is provided as a command line argument
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        try:
            deck = GameIO.read_deck_from_file(file_path)
        except Exception as e:
            print(f"Error reading deck from file: {e}")
    
    # If no deck is provided or file reading fails, initialize a new shuffled deck
    if not deck:
        deck = Deck()
        deck.shuffle()

    # Initialize and play the game
    game = Game(deck)
    game.play_game()
    
    # Output the results
    GameIO.output_game_results(game.winner, game.sam, game.dealer)

# Main execution logic
if __name__ == "__main__":
    main()
