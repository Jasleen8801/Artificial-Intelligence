# Steepest Hill Climbing Search for 8-puzzle problem

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

  def heuristicMisplacedTiles(self, state):
    cnt = 0
    for i in range(3):
      for j in range(3):
        if state[i][j] != 0 and state[i][j] != self.goal_state[i][j]:
          cnt += 1
    return cnt
  
  def heuristicManhattanDistance(self, state):
    cnt = 0
    for i in range(3):
      for j in range(3):
        if state[i][j] != 0:
          x, y = divmod(state[i][j]-1, 3)
          cnt += abs(x-i) + abs(y-j)
    return cnt
  
  def SteepestHillClimbSearch(self):
    open = self.current_state 
    closed = []
    while True:
      print(f"current state: {self.current_state}")
      if self.isGoalReached():
        print("Goal state reached!")
        return
      else:
        up = self.moveUp()
        if up != None:
          if up not in closed:
            closed.append(up)
            if self.heuristicMisplacedTiles(up) < self.heuristicMisplacedTiles(self.current_state):
              open = up
            else:
              self.current_state = self.parent
        down = self.moveDown()
        if down != None:
          if down not in closed:
            closed.append(down)
            if self.heuristicMisplacedTiles(down) < self.heuristicMisplacedTiles(self.current_state):
              open = down
            else:
              self.current_state = self.parent
        left = self.moveLeft()
        if left != None:
          if left not in closed:
            closed.append(left)
            if self.heuristicMisplacedTiles(left) < self.heuristicMisplacedTiles(self.current_state):
              open = left
            else:
              self.current_state = self.parent
        right = self.moveRight()
        if right != None:
          if right not in closed:
            closed.append(right)
            if self.heuristicMisplacedTiles(right) < self.heuristicMisplacedTiles(self.current_state):
              open = right
            else:
              self.current_state = self.parent
        print(f"open: {open}")
        print(f"closed: {closed}")
        print()
  

def main():
  my_list = [[0,1,2], [3,4,5], [6,7,8]]
  goal_list = [[1,2,3], [4,5,6], [7,8,0]]
  p1 = Puzzle(my_list, goal_list)
  p1.SteepestHillClimbSearch()
  return

if __name__ == "__main__":
  main()