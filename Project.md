# Battleship Game

Battleship Game:

In this project you will build a version of the classic board game Battleship!

#### Battleship

* The gameboard is a grid of squares. The contents of the squares are hidden from the player.

* The grid contains one or more "ships" which occupy tiles. In the simple game, a ship is a single tile big, in the full version of the game, they are short horizontal or vertical rows.

* The player attempts to attack a grid location. They are told if the attack is a miss or a hit. If all of the squares of all of the ships are hit, the player wins.

* In the two-player version of the game, the players place thier ships at the beginning of the game and then take turns attacking squares. The first player to hit all of their opponent's squares wins the game.

#### Simplified Game

* In the simple version of the game, there will be a 5x5 grid with a single "ship" that is one tile large, placed on a random tile.

* The user will be asked to guess until they hit the tile. The user will then be told how many guesses they made.

* After the user makes a guess, they see a representation of the board that indicates where they have already guessed.

* You will create a class representing the game board. A separate python file will provide the interface for the user.

* HINT: try using `os.system('clear')` to clear the terminal between inputs

#### The GameBoard class

* The gameboard should contain an internal representation of the state of the game, including where the ship is placed and where the player has guessed.

* It should have methods for guessing an attack location. What other methods will it need? What should `__init__` set? What properties will this object need to have?

#### Open-Ended Questions

* What data structures are you using to store the board? The ships?
  * What performance tradeoffs did you consider when considering which data structures to use?
  
* How are you modularizing your code? Why is a given code in Model versus View versus Controller?

* Will there be a visual component? If so, how will you dislpay information to the user?

* If you were to expand this with multiple ships of different dimensions, how would this be done? Be as specific as possible without writing code

* If you were to expand this to be multiple players, how would this be done? Be as specific as possible without writing code

