# Battleship!

The game of Battleship is played as follows:

You and your opponent are trying to find the hidden positions of the other's ships by attacking coordinates on a grid.

You and your opponent each have a hidden grid of squares. At the start of the game you place your ships, which are rectangles 1 square wide by some number of squares tall, or 1 square tall by some number of squares wide. Your ships may not overlap.

You then take turns attacking the other's grid without knowing where the ships are. Your opponent tells you whether you hit or whether you missed. If you hit the last unhit square of a ship, your opponent informs you of this.

You track your hits and misses on a second grid representing your opponent's grid.

You win the game if you have hit every square occupied by an enemy ship.

## The project

### The basic game

Create a GameBoard class. This should represent one player's grid. It should be able to place ships on itself with a method, record the opponent's hits and misses, announce when a ship is sunk and announce when it loses.

Implement a one player version where your opponent has a 5 x 5 grid that has a single, randomly placed 1x2 ship.

Write a controller and views to create an interactive terminal application that starts the game, and then prompts the player to guess squares until they have sunk the final ship. After each attack, the players should see a grid of where they have hit and where they have missed. The grid should have labeled rows and columns.

You may want to look into how to render emojis with python strings to make your game display more interesting.

### The advanced game

Have the player play against the computer. When the game starts, have them place their ship(s). Then they will take turns against the computer making attacks.

If you only have the game working with one ship, make it take multiple ships.

Come up with a way of saving application configuration in a json file. It should have options to set the size of the grid and the lengths and number of the ships. It may also have names for the ships.

Can the A.I. do better than random guessing?

Can you think of other ways to improve the game?
