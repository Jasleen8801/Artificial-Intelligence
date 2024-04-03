# Missionaries and Cannibals Problem
from collections import deque

class State:
  def __init__(self, mleft, cleft, mright, cright, boat):
    self.mleft = mleft
    self.cleft = cleft
    self.mright = mright
    self.cright = cright
    self.boat = boat
    
  def is_valid(self):
    if self.mleft<0 or self.cleft<0 or self.mright<0 or self.cright<0:
      return False
    if(self.mleft>0 and self.cleft>self.mleft) or \
      (self.mright>0 and self.cright>self.mright):
      return False
    return True
  
  def is_goal(self):
    return self.mleft==0 and self.cleft==0

def getNextMoves(state):
  moves = []
  if state.boat == 1:
    for m in range(3):
      for c in range(3):
        if 1<=m+c<=2:
          new_state = State(state.mleft-m, state.cleft-c, state.mright+m, state.cright+c, 2)
          if new_state.is_valid():
            moves.append(new_state)
  else:
    for m in range(3):
      for c in range(3):
        if 1<=m+c<=2:
          new_state = State(state.mleft+m, state.cleft+c, state.mright-m, state.cright-c, 1)
          if new_state.is_valid():
            moves.append(new_state)
  return moves

class BFS:
  def __init__(self, state) -> None:
    self.state = state
    self.closed = []
    self.open = deque()

  def search(self):
    self.open.append((self.state, []))
    while self.open:
      state, path = self.open.popleft()
      if state.is_goal():
        return path
      elif state not in self.closed:
        self.closed.append(state)
        for move in getNextMoves(state):
          self.open.append((move, path+[move]))
    return None

def main():
  state = State(3, 3, 0, 0, 1)
  bfs = BFS(state)
  path = bfs.search()
  for state in path:
    print(state.mleft, state.cleft, state.mright, state.cright, state.boat)

if __name__ == '__main__':
  main()