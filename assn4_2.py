# Best First Search for 8-puzzle problem

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
  
  def bestFirstSearch(self, heuristic):
    open_list = []
    closed_list = [] # priority queue
    open_list.append(self)

    while open_list!=[]:
      open_list.sort(key=lambda x: heuristic(x.current_state))
      current = open_list.pop(0)
      closed_list.append(current)
      current.printState(current.current_state)
      if current.isGoalReached():
        print("Goal reached")
        return
      else:
        new_state = current.moveUp()
        if new_state != None and not checkClosedList(closed_list, new_state):
          open_list.append(new_state)
          new_state.parent = current
        else:
          del new_state
        new_state = current.moveDown()
        if new_state != None and not checkClosedList(closed_list, new_state):
          open_list.append(new_state)
          new_state.parent = current
        else:
          del new_state
        new_state = current.moveLeft()
        if new_state != None and not checkClosedList(closed_list, new_state):
          open_list.append(new_state)
          new_state.parent = current
        else:
          del new_state
        new_state = current.moveRight()
        if new_state != None and not checkClosedList(closed_list, new_state):
          open_list.append(new_state)
          new_state.parent = current
        else:
          del new_state

    print("Goal not reached")
    return
  
def checkClosedList(closed_list, new_state):
  for i in range(len(closed_list)):
    if closed_list[i].current_state == new_state.current_state:
      return True
  return False

def main():
  my_list = [[2,8,1], [0,4,3], [7,6,5]]
  goal_list = [[1,2,3], [4,5,6], [7,8,0]]
  p1 = Puzzle(my_list, goal_list)
  p1.bestFirstSearch(p1.heuristicManhattanDistance)
  return

if __name__ == "__main__":
  main()