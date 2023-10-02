# Name: Ethan Wong, Angela Gerontides
# Assignment: Final Project
# We, Ethan Wong & Angela Gerontides, do hereby certify that we have derived no assistance for
# this project or examination from any sources, whether oral, written, or in print.
# References:
# - Python for Everyone (2nd Edition and 3rd Edition)

from ship import Ship
from point import Point
import random

BOARD_SIZE = 6
FLEET_SIZE = 5


class Board:
  '''
  Constructor
  ==================
  - Takes in two lists
  - The two lists represents the player's fleets
  '''

  def __init__(self, playerFleet, enemyFleet):
    self.playerBoard = [["z"] * BOARD_SIZE for i in range(BOARD_SIZE)]
    self.enemyBoard = [["z"] * BOARD_SIZE for i in range(BOARD_SIZE)]
    self.playerFleet = playerFleet
    self.enemyFleet = enemyFleet

  '''
  displayBoard()
  ==============
  - Displays the game boards to the user
  '''

  def displayBoards(self):
    print("         Player Board                   Enemy Board")
    print("    1   2   3   4   5   6           1   2   3   4   5   6")
    print("  -------------------------       -------------------------")
    for i in range(0, len(self.playerBoard)):
      # Printing the Player Board
      print(chr(ord("A") + i), end=" | ")
      for j in range(0, len(self.playerBoard[i])):
        if (self.playerBoard[i][j] == "z"):
          print(" ", end=" | ")
        else:
          print(self.playerBoard[i][j], end=" | ")

      # Printing the Enemy Board
      print("   ", chr(ord("A") + i), end=" | ")
      for j in range(0, len(self.enemyBoard[i])):
        if (self.enemyBoard[i][j].isupper()):
          print(self.enemyBoard[i][j], end=" | ")
        else:
          print(" ", end=" | ")
      print("\n  -------------------------       -------------------------\n")

  '''
  statusUpdate()
  ==============
  - Displays enemy ships' status
    - Constitutes their name, symbol, length, and how many times hit
  '''

  def statusUpdate(self):
    print("Enemy Ship Status")
    print("------------------")
    for i in range(0, FLEET_SIZE):
      (self.enemyFleet[i]).printShip()

  '''
  playerAttack
  ==================
  - Allows the player to attack a spot on the enemy's board
  - Takes in row and col in list format (ie: [0, 2])
  - Will return true if a valid attack
  - Will return false if not a valid attack
  '''

  def playerAttack(self, row, col):
    if (self.enemyBoard[row][col]).isupper():
      return False
    elif self.enemyBoard[row][col] == "z":
      print("Player misses!")
      self.enemyBoard[row][col] = "X"
      return True
    else:
      print("Player hits", end=" ")
      hitShip = self.findShip(self.enemyBoard[row][col], self.enemyFleet)
      self.enemyBoard[row][col] = (hitShip.getSymbol()).upper()
      print(hitShip.getName(), end="!\n")

      hitShip.incrementHit()
      if hitShip.isSunk():
        print("Enemy's", end=" ")
        print(hitShip.getName(), end=" has been sunk!\n")

      return True

  '''
  enemyAttack
  ==================
  - Allows the enemy to attack a spot on the player's board
  - Uses determineEnemyAttack for intelligence
  '''

  def enemyAttack(self):
    row, col = self.determineEnemyAttack()
    print("Enemy fires: " + str(Point.translateListToRow(row)) +
          str(Point.translateListToCol(col)))
    if self.playerBoard[row][col] == "z":
      self.playerBoard[row][col] = "X"
      print("Enemy misses!")
    else:
      print("Enemy hits", end=" ")
      hitShip = self.findShip(self.playerBoard[row][col].lower(),
                              self.playerFleet)
      self.playerBoard[row][col] = (hitShip.getSymbol()).upper()
      print(hitShip.getName(), end="!\n")

      hitShip.incrementHit()
      if hitShip.isSunk():
        print("Player's", end=" ")
        print(hitShip.getName(), end=" has been sunk!\n")

  '''
  determineEnemyAttack
  =====================
  - Will generate a list of all positions which are next to shot (but not sunk) ships
  - Will randomly choose one, and return its position (row, col)
    '''

  def determineEnemyAttack(self):
    allPositions = [()]
    for i in range(0, BOARD_SIZE):
      for j in range(0, BOARD_SIZE):
        if (self.playerBoard[i][j]
            ).isupper() and self.playerBoard[i][j] != "X" and (self.findShip(
              self.playerBoard[i][j].lower(), self.playerFleet)).isNotSunk():
          allPositions.extend(self.availableSurroundings(i, j))
    if len(allPositions) == 1:
      row = random.randint(0, BOARD_SIZE - 1)
      col = random.randint(0, BOARD_SIZE - 1)
      while self.playerBoard[row][col].isupper():
        row = random.randint(0, BOARD_SIZE - 1)
        col = random.randint(0, BOARD_SIZE - 1)
    else:
      randomPosition = random.randint(1, len(allPositions) - 1)
      row = allPositions[randomPosition][0]
      col = allPositions[randomPosition][1]
    return row, col

  '''
  availableSurroundings
  =====================
  - Given a position
  - Will return a 2D list of available positions next to the position given
  - Will not give positions that have already been shot at or out of bounds
  '''

  def availableSurroundings(self, row, col):
    rows = []
    cols = []

    targetShip = self.findShip(self.playerBoard[row][col].lower(),
                               self.playerFleet)
    horizontalAllow = True
    verticalAllow = True

    if targetShip.getHits() > 1:
      if targetShip.getOrientation() == "h":
        verticalAllow = False
      else:
        horizontalAllow = False

    if verticalAllow and row - 1 >= 0 and self.playerBoard[row -
                                                           1][col].islower():
      rows.append(row - 1)
      cols.append(col)
    if verticalAllow and row + 1 < BOARD_SIZE and self.playerBoard[
        row + 1][col].islower():
      rows.append(row + 1)
      cols.append(col)
    if horizontalAllow and col - 1 >= 0 and self.playerBoard[row][col -
                                                                  1].islower():
      rows.append(row)
      cols.append(col - 1)
    if horizontalAllow and col + 1 < BOARD_SIZE and self.playerBoard[row][
        col + 1].islower():
      rows.append(row)
      cols.append(col + 1)

    positions = list(zip(rows, cols))

    return positions

  '''
  populateBoard
  =================
  - Populates the game board according to two lists of Ships
  '''

  def populateBoard(self, playerFleet, enemyFleet):
    for i in range(0, len(playerFleet)):
      for j in range(0, playerFleet[i].getSize()):
        row = (playerFleet[i].getPoint(j))[0]
        col = (playerFleet[i].getPoint(j))[1]
        self.playerBoard[row][col] = playerFleet[i].getSymbol()
    for i in range(0, len(enemyFleet)):
      for j in range(0, enemyFleet[i].getSize()):
        row = (enemyFleet[i].getPoint(j))[0]
        col = (enemyFleet[i].getPoint(j))[1]
        self.enemyBoard[row][col] = enemyFleet[i].getSymbol()

  '''
  findShip
  ================
  - Takes in a symbol and a fleet (either player's or enemy's)
  - Will find the corresponding ship of symbol
  '''

  def findShip(self, symbol, fleet):
    for i in range(0, FLEET_SIZE):
      if fleet[i].getSymbol() == symbol:
        return fleet[i]
    return

  '''
  playerWin
  ==========
  - If player has won, returns true
  - If player has not won, returns false
  '''

  def playerWin(self):
    for i in range(0, FLEET_SIZE):
      if self.enemyFleet[i].isNotSunk():
        return False
    return True

  '''
  enemyWin
  ==========
  - If enemy has won, returns true
  - If enemy has not won, returns false
  '''

  def enemyWin(self):
    for i in range(0, FLEET_SIZE):
      if self.playerFleet[i].isNotSunk():
        return False
    return True

  '''
  findWinner
  ===============
  - Will determine a winner if all ships (on a board) has been sunk
  - If player wins, will return 1
  - If enemy wins, will return -1
  - If no one has won, will return 0 (will continue game)
  '''

  def findWinner(self):
    if self.playerWin():
      return 1
    elif self.enemyWin():
      return -1
    else:
      return 0
