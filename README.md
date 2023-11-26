# Blackjack Game

This is a simple command-line application that simulates a game of Blackjack between two players: Sam and the Dealer.

## Table of Contents

- [How it Works](#how-it-works)
- [How to Run](#how-to-run)
- [Testing](#testing)

## How it Works

The game is implemented using several classes that each handle a different aspect of the game:

- `Card`: Represents a playing card with a suit and a value.
- `Deck`: Represents a deck of cards. Can deal cards and be shuffled.
- `Hand`: Represents a player's hand of cards. Can calculate the score of the hand.
- `Player`: An abstract base class for a player in the game. Has a hand of cards and can decide whether to draw a card.
- `Sam` and `Dealer`: Subclasses of `Player` that implement the decision-making logic for Sam and the Dealer.
- `Game`: Controls the game logic. Deals the initial cards, controls the players' turns, and determines the winner.
- `GameIO`: Handles reading a deck of cards from a file and outputting the game results.

## Game Rules

The game is played according to the following rules:

- Each player starts with two cards.
- The score of a hand is calculated as follows: Numbered cards are their point value. Jack, Queen, and King count as 10. 
- Ace counts as 11.
- If either player has Blackjack (an initial score of 21 with two cards: A + [10, J, Q, K]) with their initial hand, they win the game.
- If both players start with Blackjack, Sam wins.
- If both players start with a score of 22 (A + A), the Dealer wins.
- If neither player has Blackjack, Sam starts drawing cards from the top of the deck.
- Sam must stop drawing cards when their total reaches 17 or higher.
- Sam loses the game if their total is higher than 21.
- When Sam has stopped drawing cards, the Dealer starts drawing cards from the top of the deck.
- The Dealer must stop drawing cards when their total is higher than Sam's.
- The Dealer loses the game if their total is higher than 21.
- The player with the highest score wins the game.

## How to Run

To run the game, you can use the `main.py` script. This script accepts an optional command-line argument specifying a file path to a text file containing a predefined deck of cards. If no file path is provided, the game will be played with a new shuffled deck.

The predefined deck file should contain a comma-separated list of cards, with each card represented by a two-character string: the first character is the suit ('S', 'H', 'D', or 'C') and the remaining characters are the value ('2'-'10', 'J', 'Q', 'K', or 'A').

Here's an example of how to run the game with a predefined deck:
```
python main.py deck.txt
```

And here's how to run the game with a new shuffled deck:
```
python main.py
```

The game will output the results to the standard output. The output will include the winner of the game and the final hands of Sam and the Dealer.

## Testing

The application includes a suite of unit tests that cover all the classes and methods. To run the tests, you can use the following command:

```
python -m unittest discover tests
```


This will discover and run all the test cases in the `tests` directory.
