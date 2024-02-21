# Lab Assignment 2
# Task 2
# 8 Puzzle problem with following initial and final states.

class Puzzle:
  def __init__(self, my_list, goal_list):
    self.current_state = my_list
    self.goal_state = goal_list
    self.empty_tile = self.getEmptyTile()
    self.parent = None

  def getEmptyTile(self): 
    for i in range(3):
      for j in range(3):
        if self.current_state[i][j] == 0:
          return (i, j)
  
  def printState(self, state):
    for i in range(3):
      for j in range(3):
        print(state[i][j], end=" ")
      print()
    print()

  def isGoalReached(self):
    return self.current_state == self.goal_state
  
  def moveUp(self):
    if self.empty_tile[0] == 0:
      return None
    else:
      # print(f"current state: {self.current_state}")
      new_state = [x[:] for x in self.current_state]
      new_state[self.empty_tile[0]][self.empty_tile[1]] = new_state[self.empty_tile[0]-1][self.empty_tile[1]]
      new_state[self.empty_tile[0]-1][self.empty_tile[1]] = 0
      self.parent = self.current_state
      self.current_state = new_state
      self.empty_tile = self.getEmptyTile()
      return new_state
    
  def moveDown(self):
    if self.empty_tile[0] == 2:
      return None
    else:
      new_state = [x[:] for x in self.current_state]
      new_state[self.empty_tile[0]][self.empty_tile[1]] = new_state[self.empty_tile[0]+1][self.empty_tile[1]]
      new_state[self.empty_tile[0]+1][self.empty_tile[1]] = 0
      self.parent = self.current_state
      self.current_state = new_state
      self.empty_tile = self.getEmptyTile()
      return new_state
    
  def moveLeft(self):
    if self.empty_tile[1] == 0:
      return None
    else:
      new_state = [x[:] for x in self.current_state]
      new_state[self.empty_tile[0]][self.empty_tile[1]] = new_state[self.empty_tile[0]][self.empty_tile[1]-1]
      new_state[self.empty_tile[0]][self.empty_tile[1]-1] = 0
      self.parent = self.current_state
      self.current_state = new_state
      self.empty_tile = self.getEmptyTile()
      return new_state
    
  def moveRight(self):
    if self.empty_tile[1] == 2:
      return None
    else:
      new_state = [x[:] for x in self.current_state]
      new_state[self.empty_tile[0]][self.empty_tile[1]] = new_state[self.empty_tile[0]][self.empty_tile[1]+1]
      new_state[self.empty_tile[0]][self.empty_tile[1]+1] = 0
      self.parent = self.current_state
      self.current_state = new_state
      # print(f"current state: {self.current_state}")
      self.empty_tile = self.getEmptyTile()
      return new_state

goal_list = [[1,2,3], [4,5,6], [7,8,9]]
my_list = [[2,8,1], [0,4,3], [7,6,5]]
puzzle = Puzzle(my_list, goal_list)
puzzle.printState(my_list)
