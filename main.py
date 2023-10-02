# Name: Ethan Wong, Angela Gerontides
# Assignment: Final Project
# We, Ethan Wong & Angela Gerontides, do hereby certify that we have derived no assistance for
# this project or examination from any sources, whether oral, written, or in print.
# References:
# - Python for Everyone (2nd Edition and 3rd Edition)

import json
from gameinterface import GameInterface
from point import Point


def main():
  runningGame = 'Y'
  while runningGame.upper() == 'Y':
    game = GameInterface("shipPositions.json")
    game.runGame()
    runningGame = input("\nWould you like to play again? (Y/N): ")
    if runningGame.upper() != 'Y' and runningGame.upper() != 'N':
      runningGame = input(
        "\nInvalid input. Would you like to play again? (Y/N): ")


if __name__ == "__main__":
  main()
'''
/Users/ethanwong/PycharmProjects/pythonProject/venv/bin/python /Users/ethanwong/PycharmProjects/pythonProject/main.py 
         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A |   | a | a | a | a | a |     A |   |   |   |   |   |   | 
  -------------------------       -------------------------

B |   |   |   | c | c | c |     B |   |   |   |   |   |   | 
  -------------------------       -------------------------

C |   |   | s |   | b |   |     C |   |   |   |   |   |   | 
  -------------------------       -------------------------

D |   |   | s |   | b |   |     D |   |   |   |   |   |   | 
  -------------------------       -------------------------

E | d | d | s |   | b |   |     E |   |   |   |   |   |   | 
  -------------------------       -------------------------

F |   |   |   |   | b |   |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------

Player please enter a coodinate: a1
Player misses!
Enemy fires: C3
Enemy hits Submarine!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 0 times
Name: Cruiser     (c)    Size: 3    Has been hit: 0 times
Name: Submarine   (s)    Size: 3    Has been hit: 0 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A |   | a | a | a | a | a |     A | X |   |   |   |   |   | 
  -------------------------       -------------------------

B |   |   |   | c | c | c |     B |   |   |   |   |   |   | 
  -------------------------       -------------------------

C |   |   | S |   | b |   |     C |   |   |   |   |   |   | 
  -------------------------       -------------------------

D |   |   | s |   | b |   |     D |   |   |   |   |   |   | 
  -------------------------       -------------------------

E | d | d | s |   | b |   |     E |   |   |   |   |   |   | 
  -------------------------       -------------------------

F |   |   |   |   | b |   |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: a2
Player misses!
Enemy fires: C4
Enemy misses!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 0 times
Name: Cruiser     (c)    Size: 3    Has been hit: 0 times
Name: Submarine   (s)    Size: 3    Has been hit: 0 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A |   | a | a | a | a | a |     A | X | X |   |   |   |   | 
  -------------------------       -------------------------

B |   |   |   | c | c | c |     B |   |   |   |   |   |   | 
  -------------------------       -------------------------

C |   |   | S | X | b |   |     C |   |   |   |   |   |   | 
  -------------------------       -------------------------

D |   |   | s |   | b |   |     D |   |   |   |   |   |   | 
  -------------------------       -------------------------

E | d | d | s |   | b |   |     E |   |   |   |   |   |   | 
  -------------------------       -------------------------

F |   |   |   |   | b |   |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: a3
Player misses!
Enemy fires: C2
Enemy misses!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 0 times
Name: Cruiser     (c)    Size: 3    Has been hit: 0 times
Name: Submarine   (s)    Size: 3    Has been hit: 0 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A |   | a | a | a | a | a |     A | X | X | X |   |   |   | 
  -------------------------       -------------------------

B |   |   |   | c | c | c |     B |   |   |   |   |   |   | 
  -------------------------       -------------------------

C |   | X | S | X | b |   |     C |   |   |   |   |   |   | 
  -------------------------       -------------------------

D |   |   | s |   | b |   |     D |   |   |   |   |   |   | 
  -------------------------       -------------------------

E | d | d | s |   | b |   |     E |   |   |   |   |   |   | 
  -------------------------       -------------------------

F |   |   |   |   | b |   |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: a4
Player misses!
Enemy fires: B3
Enemy misses!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 0 times
Name: Cruiser     (c)    Size: 3    Has been hit: 0 times
Name: Submarine   (s)    Size: 3    Has been hit: 0 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A |   | a | a | a | a | a |     A | X | X | X | X |   |   | 
  -------------------------       -------------------------

B |   |   | X | c | c | c |     B |   |   |   |   |   |   | 
  -------------------------       -------------------------

C |   | X | S | X | b |   |     C |   |   |   |   |   |   | 
  -------------------------       -------------------------

D |   |   | s |   | b |   |     D |   |   |   |   |   |   | 
  -------------------------       -------------------------

E | d | d | s |   | b |   |     E |   |   |   |   |   |   | 
  -------------------------       -------------------------

F |   |   |   |   | b |   |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: a5
Player misses!
Enemy fires: D3
Enemy hits Submarine!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 0 times
Name: Cruiser     (c)    Size: 3    Has been hit: 0 times
Name: Submarine   (s)    Size: 3    Has been hit: 0 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A |   | a | a | a | a | a |     A | X | X | X | X | X |   | 
  -------------------------       -------------------------

B |   |   | X | c | c | c |     B |   |   |   |   |   |   | 
  -------------------------       -------------------------

C |   | X | S | X | b |   |     C |   |   |   |   |   |   | 
  -------------------------       -------------------------

D |   |   | S |   | b |   |     D |   |   |   |   |   |   | 
  -------------------------       -------------------------

E | d | d | s |   | b |   |     E |   |   |   |   |   |   | 
  -------------------------       -------------------------

F |   |   |   |   | b |   |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: a6
Player misses!
Enemy fires: E3
Enemy hits Submarine!
Player's Submarine has been sunk!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 0 times
Name: Cruiser     (c)    Size: 3    Has been hit: 0 times
Name: Submarine   (s)    Size: 3    Has been hit: 0 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A |   | a | a | a | a | a |     A | X | X | X | X | X | X | 
  -------------------------       -------------------------

B |   |   | X | c | c | c |     B |   |   |   |   |   |   | 
  -------------------------       -------------------------

C |   | X | S | X | b |   |     C |   |   |   |   |   |   | 
  -------------------------       -------------------------

D |   |   | S |   | b |   |     D |   |   |   |   |   |   | 
  -------------------------       -------------------------

E | d | d | S |   | b |   |     E |   |   |   |   |   |   | 
  -------------------------       -------------------------

F |   |   |   |   | b |   |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: v1
Invalid coordinate. Please try again (ex: A4): v2
Invalid coordinate. Please try again (ex: A4): b1
Player hits Battleship!
Enemy fires: F5
Enemy hits Battleship!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 1 times
Name: Cruiser     (c)    Size: 3    Has been hit: 0 times
Name: Submarine   (s)    Size: 3    Has been hit: 0 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A |   | a | a | a | a | a |     A | X | X | X | X | X | X | 
  -------------------------       -------------------------

B |   |   | X | c | c | c |     B | B |   |   |   |   |   | 
  -------------------------       -------------------------

C |   | X | S | X | b |   |     C |   |   |   |   |   |   | 
  -------------------------       -------------------------

D |   |   | S |   | b |   |     D |   |   |   |   |   |   | 
  -------------------------       -------------------------

E | d | d | S |   | b |   |     E |   |   |   |   |   |   | 
  -------------------------       -------------------------

F |   |   |   |   | B |   |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: b2
Player hits Battleship!
Enemy fires: F4
Enemy misses!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 2 times
Name: Cruiser     (c)    Size: 3    Has been hit: 0 times
Name: Submarine   (s)    Size: 3    Has been hit: 0 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A |   | a | a | a | a | a |     A | X | X | X | X | X | X | 
  -------------------------       -------------------------

B |   |   | X | c | c | c |     B | B | B |   |   |   |   | 
  -------------------------       -------------------------

C |   | X | S | X | b |   |     C |   |   |   |   |   |   | 
  -------------------------       -------------------------

D |   |   | S |   | b |   |     D |   |   |   |   |   |   | 
  -------------------------       -------------------------

E | d | d | S |   | b |   |     E |   |   |   |   |   |   | 
  -------------------------       -------------------------

F |   |   |   | X | B |   |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: b3
Player hits Battleship!
Enemy fires: F6
Enemy misses!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 3 times
Name: Cruiser     (c)    Size: 3    Has been hit: 0 times
Name: Submarine   (s)    Size: 3    Has been hit: 0 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A |   | a | a | a | a | a |     A | X | X | X | X | X | X | 
  -------------------------       -------------------------

B |   |   | X | c | c | c |     B | B | B | B |   |   |   | 
  -------------------------       -------------------------

C |   | X | S | X | b |   |     C |   |   |   |   |   |   | 
  -------------------------       -------------------------

D |   |   | S |   | b |   |     D |   |   |   |   |   |   | 
  -------------------------       -------------------------

E | d | d | S |   | b |   |     E |   |   |   |   |   |   | 
  -------------------------       -------------------------

F |   |   |   | X | B | X |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: b4
Player hits Battleship!
Enemy's Battleship has been sunk!
Enemy fires: E5
Enemy hits Battleship!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 4 times
Name: Cruiser     (c)    Size: 3    Has been hit: 0 times
Name: Submarine   (s)    Size: 3    Has been hit: 0 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A |   | a | a | a | a | a |     A | X | X | X | X | X | X | 
  -------------------------       -------------------------

B |   |   | X | c | c | c |     B | B | B | B | B |   |   | 
  -------------------------       -------------------------

C |   | X | S | X | b |   |     C |   |   |   |   |   |   | 
  -------------------------       -------------------------

D |   |   | S |   | b |   |     D |   |   |   |   |   |   | 
  -------------------------       -------------------------

E | d | d | S |   | B |   |     E |   |   |   |   |   |   | 
  -------------------------       -------------------------

F |   |   |   | X | B | X |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: b5
Player misses!
Enemy fires: D5
Enemy hits Battleship!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 4 times
Name: Cruiser     (c)    Size: 3    Has been hit: 0 times
Name: Submarine   (s)    Size: 3    Has been hit: 0 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A |   | a | a | a | a | a |     A | X | X | X | X | X | X | 
  -------------------------       -------------------------

B |   |   | X | c | c | c |     B | B | B | B | B | X |   | 
  -------------------------       -------------------------

C |   | X | S | X | b |   |     C |   |   |   |   |   |   | 
  -------------------------       -------------------------

D |   |   | S |   | B |   |     D |   |   |   |   |   |   | 
  -------------------------       -------------------------

E | d | d | S |   | B |   |     E |   |   |   |   |   |   | 
  -------------------------       -------------------------

F |   |   |   | X | B | X |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: b6
Player misses!
Enemy fires: C5
Enemy hits Battleship!
Player's Battleship has been sunk!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 4 times
Name: Cruiser     (c)    Size: 3    Has been hit: 0 times
Name: Submarine   (s)    Size: 3    Has been hit: 0 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A |   | a | a | a | a | a |     A | X | X | X | X | X | X | 
  -------------------------       -------------------------

B |   |   | X | c | c | c |     B | B | B | B | B | X | X | 
  -------------------------       -------------------------

C |   | X | S | X | B |   |     C |   |   |   |   |   |   | 
  -------------------------       -------------------------

D |   |   | S |   | B |   |     D |   |   |   |   |   |   | 
  -------------------------       -------------------------

E | d | d | S |   | B |   |     E |   |   |   |   |   |   | 
  -------------------------       -------------------------

F |   |   |   | X | B | X |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: c1
Player misses!
Enemy fires: A5
Enemy hits Carrier!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 4 times
Name: Cruiser     (c)    Size: 3    Has been hit: 0 times
Name: Submarine   (s)    Size: 3    Has been hit: 0 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A |   | a | a | a | A | a |     A | X | X | X | X | X | X | 
  -------------------------       -------------------------

B |   |   | X | c | c | c |     B | B | B | B | B | X | X | 
  -------------------------       -------------------------

C |   | X | S | X | B |   |     C | X |   |   |   |   |   | 
  -------------------------       -------------------------

D |   |   | S |   | B |   |     D |   |   |   |   |   |   | 
  -------------------------       -------------------------

E | d | d | S |   | B |   |     E |   |   |   |   |   |   | 
  -------------------------       -------------------------

F |   |   |   | X | B | X |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: c2
Player misses!
Enemy fires: A4
Enemy hits Carrier!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 4 times
Name: Cruiser     (c)    Size: 3    Has been hit: 0 times
Name: Submarine   (s)    Size: 3    Has been hit: 0 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A |   | a | a | A | A | a |     A | X | X | X | X | X | X | 
  -------------------------       -------------------------

B |   |   | X | c | c | c |     B | B | B | B | B | X | X | 
  -------------------------       -------------------------

C |   | X | S | X | B |   |     C | X | X |   |   |   |   | 
  -------------------------       -------------------------

D |   |   | S |   | B |   |     D |   |   |   |   |   |   | 
  -------------------------       -------------------------

E | d | d | S |   | B |   |     E |   |   |   |   |   |   | 
  -------------------------       -------------------------

F |   |   |   | X | B | X |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: c3
Player hits Cruiser!
Enemy fires: A6
Enemy hits Carrier!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 4 times
Name: Cruiser     (c)    Size: 3    Has been hit: 1 times
Name: Submarine   (s)    Size: 3    Has been hit: 0 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A |   | a | a | A | A | A |     A | X | X | X | X | X | X | 
  -------------------------       -------------------------

B |   |   | X | c | c | c |     B | B | B | B | B | X | X | 
  -------------------------       -------------------------

C |   | X | S | X | B |   |     C | X | X | C |   |   |   | 
  -------------------------       -------------------------

D |   |   | S |   | B |   |     D |   |   |   |   |   |   | 
  -------------------------       -------------------------

E | d | d | S |   | B |   |     E |   |   |   |   |   |   | 
  -------------------------       -------------------------

F |   |   |   | X | B | X |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: c4
Player hits Cruiser!
Enemy fires: A3
Enemy hits Carrier!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 4 times
Name: Cruiser     (c)    Size: 3    Has been hit: 2 times
Name: Submarine   (s)    Size: 3    Has been hit: 0 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A |   | a | A | A | A | A |     A | X | X | X | X | X | X | 
  -------------------------       -------------------------

B |   |   | X | c | c | c |     B | B | B | B | B | X | X | 
  -------------------------       -------------------------

C |   | X | S | X | B |   |     C | X | X | C | C |   |   | 
  -------------------------       -------------------------

D |   |   | S |   | B |   |     D |   |   |   |   |   |   | 
  -------------------------       -------------------------

E | d | d | S |   | B |   |     E |   |   |   |   |   |   | 
  -------------------------       -------------------------

F |   |   |   | X | B | X |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: c5
Player hits Cruiser!
Enemy's Cruiser has been sunk!
Enemy fires: A2
Enemy hits Carrier!
Player's Carrier has been sunk!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 4 times
Name: Cruiser     (c)    Size: 3    Has been hit: 3 times
Name: Submarine   (s)    Size: 3    Has been hit: 0 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A |   | A | A | A | A | A |     A | X | X | X | X | X | X | 
  -------------------------       -------------------------

B |   |   | X | c | c | c |     B | B | B | B | B | X | X | 
  -------------------------       -------------------------

C |   | X | S | X | B |   |     C | X | X | C | C | C |   | 
  -------------------------       -------------------------

D |   |   | S |   | B |   |     D |   |   |   |   |   |   | 
  -------------------------       -------------------------

E | d | d | S |   | B |   |     E |   |   |   |   |   |   | 
  -------------------------       -------------------------

F |   |   |   | X | B | X |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: c6
Player misses!
Enemy fires: A1
Enemy misses!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 4 times
Name: Cruiser     (c)    Size: 3    Has been hit: 3 times
Name: Submarine   (s)    Size: 3    Has been hit: 0 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A | X | A | A | A | A | A |     A | X | X | X | X | X | X | 
  -------------------------       -------------------------

B |   |   | X | c | c | c |     B | B | B | B | B | X | X | 
  -------------------------       -------------------------

C |   | X | S | X | B |   |     C | X | X | C | C | C | X | 
  -------------------------       -------------------------

D |   |   | S |   | B |   |     D |   |   |   |   |   |   | 
  -------------------------       -------------------------

E | d | d | S |   | B |   |     E |   |   |   |   |   |   | 
  -------------------------       -------------------------

F |   |   |   | X | B | X |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: d1
Player hits Submarine!
Enemy fires: F1
Enemy misses!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 4 times
Name: Cruiser     (c)    Size: 3    Has been hit: 3 times
Name: Submarine   (s)    Size: 3    Has been hit: 1 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A | X | A | A | A | A | A |     A | X | X | X | X | X | X | 
  -------------------------       -------------------------

B |   |   | X | c | c | c |     B | B | B | B | B | X | X | 
  -------------------------       -------------------------

C |   | X | S | X | B |   |     C | X | X | C | C | C | X | 
  -------------------------       -------------------------

D |   |   | S |   | B |   |     D | S |   |   |   |   |   | 
  -------------------------       -------------------------

E | d | d | S |   | B |   |     E |   |   |   |   |   |   | 
  -------------------------       -------------------------

F | X |   |   | X | B | X |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: d2
Player hits Submarine!
Enemy fires: D4
Enemy misses!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 4 times
Name: Cruiser     (c)    Size: 3    Has been hit: 3 times
Name: Submarine   (s)    Size: 3    Has been hit: 2 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A | X | A | A | A | A | A |     A | X | X | X | X | X | X | 
  -------------------------       -------------------------

B |   |   | X | c | c | c |     B | B | B | B | B | X | X | 
  -------------------------       -------------------------

C |   | X | S | X | B |   |     C | X | X | C | C | C | X | 
  -------------------------       -------------------------

D |   |   | S | X | B |   |     D | S | S |   |   |   |   | 
  -------------------------       -------------------------

E | d | d | S |   | B |   |     E |   |   |   |   |   |   | 
  -------------------------       -------------------------

F | X |   |   | X | B | X |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: d3
Player hits Submarine!
Enemy's Submarine has been sunk!
Enemy fires: B1
Enemy misses!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 4 times
Name: Cruiser     (c)    Size: 3    Has been hit: 3 times
Name: Submarine   (s)    Size: 3    Has been hit: 3 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A | X | A | A | A | A | A |     A | X | X | X | X | X | X | 
  -------------------------       -------------------------

B | X |   | X | c | c | c |     B | B | B | B | B | X | X | 
  -------------------------       -------------------------

C |   | X | S | X | B |   |     C | X | X | C | C | C | X | 
  -------------------------       -------------------------

D |   |   | S | X | B |   |     D | S | S | S |   |   |   | 
  -------------------------       -------------------------

E | d | d | S |   | B |   |     E |   |   |   |   |   |   | 
  -------------------------       -------------------------

F | X |   |   | X | B | X |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: d4
Player misses!
Enemy fires: B5
Enemy hits Cruiser!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 4 times
Name: Cruiser     (c)    Size: 3    Has been hit: 3 times
Name: Submarine   (s)    Size: 3    Has been hit: 3 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A | X | A | A | A | A | A |     A | X | X | X | X | X | X | 
  -------------------------       -------------------------

B | X |   | X | c | C | c |     B | B | B | B | B | X | X | 
  -------------------------       -------------------------

C |   | X | S | X | B |   |     C | X | X | C | C | C | X | 
  -------------------------       -------------------------

D |   |   | S | X | B |   |     D | S | S | S | X |   |   | 
  -------------------------       -------------------------

E | d | d | S |   | B |   |     E |   |   |   |   |   |   | 
  -------------------------       -------------------------

F | X |   |   | X | B | X |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: d5
Player misses!
Enemy fires: B6
Enemy hits Cruiser!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 4 times
Name: Cruiser     (c)    Size: 3    Has been hit: 3 times
Name: Submarine   (s)    Size: 3    Has been hit: 3 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A | X | A | A | A | A | A |     A | X | X | X | X | X | X | 
  -------------------------       -------------------------

B | X |   | X | c | C | C |     B | B | B | B | B | X | X | 
  -------------------------       -------------------------

C |   | X | S | X | B |   |     C | X | X | C | C | C | X | 
  -------------------------       -------------------------

D |   |   | S | X | B |   |     D | S | S | S | X | X |   | 
  -------------------------       -------------------------

E | d | d | S |   | B |   |     E |   |   |   |   |   |   | 
  -------------------------       -------------------------

F | X |   |   | X | B | X |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: d6
Player misses!
Enemy fires: B4
Enemy hits Cruiser!
Player's Cruiser has been sunk!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 4 times
Name: Cruiser     (c)    Size: 3    Has been hit: 3 times
Name: Submarine   (s)    Size: 3    Has been hit: 3 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A | X | A | A | A | A | A |     A | X | X | X | X | X | X | 
  -------------------------       -------------------------

B | X |   | X | C | C | C |     B | B | B | B | B | X | X | 
  -------------------------       -------------------------

C |   | X | S | X | B |   |     C | X | X | C | C | C | X | 
  -------------------------       -------------------------

D |   |   | S | X | B |   |     D | S | S | S | X | X | X | 
  -------------------------       -------------------------

E | d | d | S |   | B |   |     E |   |   |   |   |   |   | 
  -------------------------       -------------------------

F | X |   |   | X | B | X |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: e1
Player misses!
Enemy fires: D2
Enemy misses!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 4 times
Name: Cruiser     (c)    Size: 3    Has been hit: 3 times
Name: Submarine   (s)    Size: 3    Has been hit: 3 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A | X | A | A | A | A | A |     A | X | X | X | X | X | X | 
  -------------------------       -------------------------

B | X |   | X | C | C | C |     B | B | B | B | B | X | X | 
  -------------------------       -------------------------

C |   | X | S | X | B |   |     C | X | X | C | C | C | X | 
  -------------------------       -------------------------

D |   | X | S | X | B |   |     D | S | S | S | X | X | X | 
  -------------------------       -------------------------

E | d | d | S |   | B |   |     E | X |   |   |   |   |   | 
  -------------------------       -------------------------

F | X |   |   | X | B | X |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: e2
Player misses!
Enemy fires: E2
Enemy hits Destroyer!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 4 times
Name: Cruiser     (c)    Size: 3    Has been hit: 3 times
Name: Submarine   (s)    Size: 3    Has been hit: 3 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A | X | A | A | A | A | A |     A | X | X | X | X | X | X | 
  -------------------------       -------------------------

B | X |   | X | C | C | C |     B | B | B | B | B | X | X | 
  -------------------------       -------------------------

C |   | X | S | X | B |   |     C | X | X | C | C | C | X | 
  -------------------------       -------------------------

D |   | X | S | X | B |   |     D | S | S | S | X | X | X | 
  -------------------------       -------------------------

E | d | D | S |   | B |   |     E | X | X |   |   |   |   | 
  -------------------------       -------------------------

F | X |   |   | X | B | X |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: e3
Player misses!
Enemy fires: F2
Enemy misses!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 4 times
Name: Cruiser     (c)    Size: 3    Has been hit: 3 times
Name: Submarine   (s)    Size: 3    Has been hit: 3 times
Name: Destroyer   (d)    Size: 2    Has been hit: 0 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A | X | A | A | A | A | A |     A | X | X | X | X | X | X | 
  -------------------------       -------------------------

B | X |   | X | C | C | C |     B | B | B | B | B | X | X | 
  -------------------------       -------------------------

C |   | X | S | X | B |   |     C | X | X | C | C | C | X | 
  -------------------------       -------------------------

D |   | X | S | X | B |   |     D | S | S | S | X | X | X | 
  -------------------------       -------------------------

E | d | D | S |   | B |   |     E | X | X | X |   |   |   | 
  -------------------------       -------------------------

F | X | X |   | X | B | X |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------


Player please enter a coodinate: e4
Player hits Destroyer!
Enemy fires: E1
Enemy hits Destroyer!
Player's Destroyer has been sunk!

Enemy Ship Status
------------------
Name: Carrier     (a)    Size: 5    Has been hit: 0 times
Name: Battleship  (b)    Size: 4    Has been hit: 4 times
Name: Cruiser     (c)    Size: 3    Has been hit: 3 times
Name: Submarine   (s)    Size: 3    Has been hit: 3 times
Name: Destroyer   (d)    Size: 2    Has been hit: 1 times

         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A | X | A | A | A | A | A |     A | X | X | X | X | X | X | 
  -------------------------       -------------------------

B | X |   | X | C | C | C |     B | B | B | B | B | X | X | 
  -------------------------       -------------------------

C |   | X | S | X | B |   |     C | X | X | C | C | C | X | 
  -------------------------       -------------------------

D |   | X | S | X | B |   |     D | S | S | S | X | X | X | 
  -------------------------       -------------------------

E | D | D | S |   | B |   |     E | X | X | X | D |   |   | 
  -------------------------       -------------------------

F | X | X |   | X | B | X |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------



ENEMY WINS!

Would you like to play again? (Y/N): e5

Invalid input. Would you like to play again? (Y/N): y
         Player Board                   Enemy Board
    1   2   3   4   5   6           1   2   3   4   5   6
  -------------------------       -------------------------
A | a | a | a | a | a |   |     A |   |   |   |   |   |   | 
  -------------------------       -------------------------

B |   | b |   |   |   |   |     B |   |   |   |   |   |   | 
  -------------------------       -------------------------

C |   | b |   |   |   |   |     C |   |   |   |   |   |   | 
  -------------------------       -------------------------

D |   | b |   |   |   |   |     D |   |   |   |   |   |   | 
  -------------------------       -------------------------

E |   | b |   | d | d |   |     E |   |   |   |   |   |   | 
  -------------------------       -------------------------

F | s | s | s | c | c | c |     F |   |   |   |   |   |   | 
  -------------------------       -------------------------

Player please enter a coodinate: 
'''

# Note: The code cuts off as I forcefully stopped the program there
