# Lab Assignment 2
# Task 2: 8 Puzzle Problem

class Puzzle:
  def __init__(self, board):
    self.board = board
    self.goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

  def printState(self):
    print(f"{self.board[0]} {self.board[1]} {self.board[2]}\n{self.board[3]} {self.board[4]} {self.board[5]}\n{self.board[6]} {self.board[7]} {self.board[8]}")

  def isGoal(self):
    return self.board == self.goal
  
  def getEmptyTile(self, board):
    for i in range(9):
      if board[i] == 0:
        return i
      
  def moveUp(self):
    empty_tile = self.getEmptyTile(self.board)
    if empty_tile < 3:
      return None
    else:
      new_board = self.board.copy()
      new_board[empty_tile] = new_board[empty_tile-3]
      new_board[empty_tile-3] = 0
      return new_board
    
  def moveDown(self):
    empty_tile = self.getEmptyTile(self.board)
    if empty_tile > 5:
      return None
    else:
      new_board = self.board.copy()
      new_board[empty_tile] = new_board[empty_tile+3]
      new_board[empty_tile+3] = 0
      return new_board
    
  def moveLeft(self):
    empty_tile = self.getEmptyTile(self.board)
    if empty_tile % 3 == 0:
      return None
    else:
      new_board = self.board.copy()
      new_board[empty_tile] = new_board[empty_tile-1]
      new_board[empty_tile-1] = 0
      return new_board
    
  def moveRight(self):
    empty_tile = self.getEmptyTile(self.board)
    if empty_tile % 3 == 2:
      return None
    else:
      new_board = self.board.copy()
      new_board[empty_tile] = new_board[empty_tile+1]
      new_board[empty_tile+1] = 0
      return new_board
    
  def move(self, direction):
    if direction == 1:
      return self.moveUp()
    elif direction == 2:
      return self.moveDown()
    elif direction == 3:
      return self.moveLeft()
    elif direction == 4:
      return self.moveRight()
    
def main():
  board = [1, 2, 3, 4, 5, 6, 7, 0, 8]
  puzzle = Puzzle(board)
  puzzle.printState()
  print(puzzle.isGoal())
  print(puzzle.move(1))
  print(puzzle.move(2))
  print(puzzle.move(3))
  print(puzzle.move(4))

if __name__ == "__main__":
  main()