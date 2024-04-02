import copy

class Puzzle:
  def __init__(self, initial, goal):
    self.initial = initial
    self.goal = goal

  def getBlankState(self, state):
    for i in range(3):
      for j in range(3):
        if state[i][j]==0:
          return (i,j)
        
  def moveLeft(self, state):
    blank = self.getBlankState(state)
    if blank[1]>0:
      new_state = copy.deepcopy(state)
      new_state[blank[0]][blank[1]] = new_state[blank[0]][blank[1]-1]
      new_state[blank[0]][blank[1]-1] = 0
      return new_state
    else:
      return None
  
  def moveRight(self, state):
    blank = self.getBlankState(state)
    if blank[1]<2:
      new_state = copy.deepcopy(state)
      new_state[blank[0]][blank[1]] = new_state[blank[0]][blank[1]+1]
      new_state[blank[0]][blank[1]+1] = 0
      return new_state
    else:
      return None
    
  def moveUp(self, state):
    blank = self.getBlankState(state)
    if blank[0]>0:
      new_state = copy.deepcopy(state)
      new_state[blank[0]][blank[1]] = new_state[blank[0]-1][blank[1]]
      new_state[blank[0]-1][blank[1]] = 0
      return new_state
    else:
      return None
    
  def moveDown(self, state):
    blank = self.getBlankState(state)
    if blank[0]<2:
      new_state = copy.deepcopy(state)
      new_state[blank[0]][blank[1]] = new_state[blank[0]+1][blank[1]]
      new_state[blank[0]+1][blank[1]] = 0
      return new_state
    else:
      return None
    
  def getNextMove(self, state):
    moves = []
    moves.append(self.moveLeft(state))
    moves.append(self.moveRight(state))
    moves.append(self.moveUp(state))
    moves.append(self.moveDown(state))
    return moves
  
  def printState(self, state):
    for i in range(3):
      for j in range(3):
        print(state[i][j], end=" ")
      print()
    print()

def main():
  initial = [[1,2,3],[4,5,6],[7,0,8]]
  goal = [[1,2,3],[4,5,6],[7,8,0]]
  puzzle = Puzzle(initial, goal)
  puzzle.printState(initial)
  puzzle.printState(goal)
  print(puzzle.getNextMove(initial))

if __name__ == '__main__':
  main()