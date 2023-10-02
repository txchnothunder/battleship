# Name: Ethan Wong, Angela Gerontides
# Assignment: Final Project
# We, Ethan Wong & Angela Gerontides, do hereby certify that we have derived no assistance for
# this project or examination from any sources, whether oral, written, or in print.
# References:
# - Python for Everyone (2nd Edition and 3rd Edition)


class Ship:
  '''
  Constructor
  ===========
  - Constructs a Ship object
  - Takes in a name, size, orientation, the points (position of the ship), and symbol
    '''

  def __init__(self, name, size, orientation, points, symbol):
    self.name = name
    self.size = size
    self.orientation = orientation
    self.currentHitCount = 0
    self.points = points
    self.symbol = symbol

  '''
  printShip()
  ===========
  - Will prints the ship information
  - ie. Name, Size, Symbol, and Hit Count
  - DOES NOT display orientation and points
  '''

  def printShip(self):
    print("Name:", end=" ")
    print(self.name, end="")
    for i in range(len(self.name), 12):
      print(end=" ")
    print("(", end="")
    print(self.symbol, end=")    ")
    print("Size:", self.size, end="    ")
    print("Has been hit:", self.currentHitCount, end=" times\n")

  '''
  getName()
  =========
  - Returns the name
    '''

  def getName(self):
    return self.name

  '''
  getSize()
  =========
  - Returns the size
  '''

  def getSize(self):
    return self.size

  '''
  getOrientation()
  =================
  - Returns the orientation
  '''

  def getOrientation(self):
    return self.orientation

  '''
  getPoints()
  ============
  - Returns a list of all the points
  '''

  def getPoints(self):
    return self.points

  '''
  getPoint
  ===============
  - Gets a singular point at a specific position
  - Ex: [[0,0], [0,1], [0,2]], position 2 would return [0,2]
  '''

  def getPoint(self, position):
    return self.points[position]

  '''
  getSymbol()
  ===========
  - Returns the symbol
  '''

  def getSymbol(self):
    return self.symbol

  '''
  getHits()
  =========
  - Returns the hits
  '''

  def getHits(self):
    return self.currentHitCount

  '''
  incrementHit()
  ===============
  - Will increment the hit count by 1
    '''

  def incrementHit(self):
    self.currentHitCount += 1

  '''
  isSunk()
  ============
  - If the ship is sunk, will return true
  - If the ship is not sunk, will return false
  '''

  def isSunk(self):
    if self.getHits() >= self.getSize():
      return True
    else:
      return False

  '''
  isNotSunk()
  ============
  - If the ship is not sunk, will return true
  - If the ship is sunk, will return false
  '''

  def isNotSunk(self):
    return not self.isSunk()
