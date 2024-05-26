# Naughts And Crosses Game 
## By Nitzan Ainemer

This is a simple Naughts and Crosses games, for 2 players on a single computer.

## Running the game:

### Mac:
1. Right Click ``NaughtsAndCrosses.app``
2. Select ``Open`` from context menu

### Windows:

1. Double-Click ``NaughtsAndCrosses.exe``
2. If a security warning appears, Click ``More Info``
3. Click ``Run Anyway``

## Implementation and Design

### Implementation:

The game is implemented in Python, using basic included tools of python like tkinter for GUI.

### Design

The project built using OOP principles. The code is Modular - there are different modules that responsible for different parts of the game.
For example, the ``game module`` is responsible for managing the logic of the game, according to the user input to the ``GUI module``.
The game module implements Encapsulation by encapsulation methods and classes within, like ``Board``, ``Stats`` and ``Player``.
The ``game module`` also manages the turn change, manages the board, check for the results and updates statistics.

For each element in the code, I implemented a module and a class to keep abstraction and modularity of the code. Some classes have more logic (Like ``NntGui`` and ``Game``) and some are thinner like ``Player`` and ``Cell``.

My code is designed to be easy to: 
1. understand (by using constants, documentation, abstraction and encapsulation)
2. maintain (by separating the code to different small modules)
3. add new features (by keeping the logic abstract and separated and not concrete about the normal 'well known' version of the game)




For the source code, visit my github: https://github.com/nitzan63/NaughtsAndCrosses/

