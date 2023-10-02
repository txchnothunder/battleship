# Name: Ethan Wong, Angela Gerontides
# Assignment: Final Project
# We, Ethan Wong & Angela Gerontides, do hereby certify that we have derived no assistance for
# this project or examination from any sources, whether oral, written, or in print.
# References:
# - Python for Everyone (2nd Edition and 3rd Edition)

import json
import random
from board import Board
from point import Point
from ship import Ship

SHIP_NAMES = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
BOARD_SIZE = 6


class GameInterface:
  '''
  Constructor
  ===========
  - Takes in a string, which represents the json file
  '''

  def __init__(self, jsonFile):
    self.jsonFile = jsonFile

  '''
  runGame()
  ==========
  - Will run the game
  '''

  def runGame(self):
    # Reading JSON Files and Making Ships

    # Player Ships
    playerFleet = []
    with open(self.jsonFile, "r") as read_file:
      obj = json.load(read_file)
      randomPlayerBoard = random.randint(0, 9)
      obj = obj[randomPlayerBoard]
      for i in range(0, len(SHIP_NAMES)):
        name = SHIP_NAMES[i]
        size = obj[name]["Size"]
        orientation = obj[name]["Orientation"]
        position = obj[name]["Position"]
        symbol = obj[name]["Symbol"]
        s = Ship(name, size, orientation, position, symbol)
        playerFleet.append(s)

    # Enemy Ships
    enemyFleet = []
    with open(self.jsonFile, "r") as read_file:
      obj = json.load(read_file)
      randomEnemyBoard = random.randint(0, 9)
      while (randomEnemyBoard == randomPlayerBoard):
        randomEnemyBoard = random.randint(0, 9)
      obj = obj[randomEnemyBoard]
      for i in range(0, len(SHIP_NAMES)):
        name = SHIP_NAMES[i]
        size = obj[name]["Size"]
        orientation = obj[name]["Orientation"]
        position = obj[name]["Position"]
        symbol = obj[name]["Symbol"]
        s = Ship(name, size, orientation, position, symbol)
        enemyFleet.append(s)

    boards = Board(playerFleet, enemyFleet)
    boards.populateBoard(playerFleet, enemyFleet)
    boards.displayBoards()

    while boards.findWinner() == 0:
      rowPlayerGuess, columnPlayerGuess = self.getPlayerGuesses()
      while not boards.playerAttack(rowPlayerGuess, columnPlayerGuess):
        print("This position has already been shot. Try again.")
        rowPlayerGuess, columnPlayerGuess = self.getPlayerGuesses()

      if boards.findWinner() != 0:
        break

      boards.enemyAttack()

      print()
      boards.statusUpdate()
      print()
      boards.displayBoards()
      print()

    if boards.findWinner() == 1:
      print("\nPLAYER WINS!")
    if boards.findWinner() == -1:
      print("\nENEMY WINS!")

  '''
  getPlayerGuesses()
  ==================
  - Gets the player input for their guess
  - Will return a VALID player input
  - If an invalid input is received, it'll ask again
  '''

  def getPlayerGuesses(self):
    coordinate = input("Player please enter a coodinate: ")
    while len(coordinate) != 2 or ord(coordinate[0].upper()) < ord("A") or ord(
        coordinate[0].upper()) > ord("F") or ord(
          coordinate[1]) < ord("1") or ord(coordinate[1]) > ord("6"):
      coordinate = input("Invalid coordinate. Please try again (ex: A4): ")

    row = Point.translateRowToList(coordinate[0].upper())
    column = Point.translateColToList(coordinate[1])

    return row, column
