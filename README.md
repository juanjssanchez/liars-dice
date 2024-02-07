# Liars Dice Game

## Description

This is a Python implementation of the Liars Dice game. Liars Dice is a dice game where players roll dice and make bids on the result of all players' dice rolls combined. Players take turns bidding on the quantity of dice showing a certain face value, with each bid required to be higher than the previous one. The game involves bluffing and deduction, as players must decide whether to trust the bids made by others or to challenge them as liars.

## How to Play

1. **Setup**: Each player starts with a set number of dice (5). The game requires at least two players.

2. **Roll Dice**: Players roll their dice, keeping the results hidden from other players.

3. **Make Bids**: Starting with one player, each player makes a bid on the quantity of dice showing a specific face value (e.g., "3 fours"). The next player must either raise the bid (with a higher quantity or face value) or call the previous bid a bluff.

4. **Challenge or Accept**: If a player believes the previous bid is incorrect, they can challenge it by calling. All dice are revealed, and if the bid was indeed incorrect, the bidder loses a die. If the bid was accurate, the challenger loses a die.

5. **Continue**: The game continues until only one player remains with dice remaining.

## Running the Game

To play the Liars Dice game:

1. Clone the repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the game files.

3. Run the Python script `liars_dice.py`.

4. Follow the on-screen instructions to enter the number of players and player names.

5. Play the game by following the prompts to make bids and challenge other CPU players.

## Requirements

- Python 3.x
- Random module (comes pre-installed with Python)

