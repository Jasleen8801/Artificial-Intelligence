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
  
  def move(self, pos):
    pass