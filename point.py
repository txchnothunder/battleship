# Name: Ethan Wong, Angela Gerontides
# Assignment: Final Project
# We, Ethan Wong & Angela Gerontides, do hereby certify that we have derived no assistance for
# this project or examination from any sources, whether oral, written, or in print.
# References:
# - Python for Everyone (2nd Edition and 3rd Edition)
'''
Class will receive position in user coordinates (ie: A3) and will translate it to program coordinates (ie: [0, 2])
'''


class Point:
  '''
    Constructor
    ===========
    - Gets position in user coordinates
    - User coordinate format must be correct
      - First char must be an uppercase letter from A-F
      - Second char must be an integer from 1-6
      - Must have only two characters
    '''

  def __init__(self, position):
    self.row = str(position[0])
    self.col = int(position[1])

  '''
    translateRowToList
    ==================
    - Translates the row to program coordinates
    '''

  @classmethod
  def translateRowToList(
    cls, row
  ):  # convention to uppercase class method to distinguish it from a instance/object method
    return ord(row) - ord("A")

  '''
    translateColToList
    ==================
    - Translates the col to program coordinates
    '''

  @classmethod
  def translateColToList(
    cls, col
  ):  # convention to uppercase class method to distinguish it from a instance/object method
    return int(col) - 1

  """
    translateListToRow
    ==================
    - Translates the list point to row display coordinate
    """

  @classmethod
  def translateListToRow(cls, x):
    return chr(ord("A") + x)

  """
    translateListToCol
    ==================
    - Translates the list point to column display coordinate 
    """

  @classmethod
  def translateListToCol(
    cls, y
  ):  # convention to uppercase class method to distinguish it from a instance/object method
    return y + 1
