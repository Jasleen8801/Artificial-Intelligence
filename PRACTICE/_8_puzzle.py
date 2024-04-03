import copy
from collections import deque 
from queue import PriorityQueue
import random

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

  def heuristic(self, state):
    cnt = 0
    for i in range(3):
      for j in range(3):
        if state[i][j] == self.goal[i][j]:
          cnt += 1
    return cnt

class BFS:
  def __init__(self, puzzle) -> None:
    self.puzzle = puzzle
    self.closed = []
    self.open = deque()

  def search(self):
    self.open.append((self.puzzle.initial, []))
    while self.open:
      state, path = self.open.popleft()
      if state==self.puzzle.goal:
        return path
      elif str(state) not in self.closed:
        self.closed.append(str(state))
        for move in self.puzzle.getNextMove(state):
          if move is not None:
            self.open.append((move, path+[move]))

class DFS:
  def __init__(self, puzzle):
    self.puzzle = puzzle
    self.closed = []
    self.open = []

  def search(self):
    self.open.append((self.puzzle.initial, []))

    while self.open:
      state, path = self.open.pop()
      if state == self.puzzle.goal:
        return path
      elif str(state) not in self.closed:
        self.closed.append(str(state))
        for next_state in reversed(self.puzzle.getNextMove(state)):
          if next_state is not None:
            self.open.append((next_state, path + [next_state]))

    return None

class DFSL:
  def __init__(self, puzzle, level):
    self.puzzle = puzzle
    self.closed = []
    self.open = []
    self.level = level

  def search(self):
    self.open.append((self.puzzle.initial, []))
    while self.open:
      state, path = self.open.pop()
      if state==self.puzzle.goal:
        return path
      elif str(state) not in self.closed:
        self.closed.append(str(state))
        if len(path)<self.level:
          for move in self.puzzle.getNextMove(state):
            if move is not None:
              self.open.append((move, path+[move]))
    return None

class DFSID:
  def __init__(self, puzzle):
    self.puzzle = puzzle
    self.closed = []
    self.open = []
    self.level = 0

  def search(self):
    while True:
      self.open.append((self.puzzle.initial, []))
      while self.open:
        state, path = self.open.pop()
        if state==self.puzzle.goal:
          return path
        elif str(state) not in self.closed:
          self.closed.append(str(state))
          if len(path)<self.level:
            for move in self.puzzle.getNextMove(state):
              if move is not None:
                self.open.append((move, path+[move]))
      self.level += 1

class UCS:
  def __init__(self, puzzle):
    self.puzzle = puzzle
    self.closed = []
    self.open = PriorityQueue()

  def search(self):
    self.open.put((0, self.puzzle.initial, []))
    while not self.open.empty():
      cost, state, path = self.open.get()
      if state == self.puzzle.goal:
        return path
      elif str(state) not in self.closed:
        self.closed.append(str(state))
        for move in self.puzzle.getNextMove(state):
          if move is not None:
            self.open.put((cost+1, move, path+[move]))

class SimpleHillClimb:
  def __init__(self, puzzle):
    self.puzzle = puzzle
  
  def search(self):
    curr = self.puzzle.initial
    path = [curr]

    while True:
      h = self.puzzle.heuristic(curr)
      if h==9: # goal state
        return path
      
      moves = self.puzzle.getNextMove(curr)
      moves = [move for move in moves if move is not None]  
      if moves is None:
        print('Failed to find solution')
        return path
      h_next = [self.puzzle.heuristic(move) for move in moves]

      if max(h_next) < h:
        print('Stuck at local maxima')
        return path
      
      if moves is None:
        print('Failed to find solution')
        return path
      
      indices = [i for i,j in enumerate(h_next) if j>h] 
      choice = random.choice(indices)

      curr = moves[choice]
      path.append(curr)

class BestFirstSearch:
  def __init__(self, puzzle):
    self.puzzle = puzzle
    self.closed = []
    self.open = PriorityQueue()

  def search(self):
    self.open.put((self.puzzle.heuristic(self.puzzle.initial), self.puzzle.initial, []))
    while not self.open.empty():
      cost, state, path = self.open.get()
      if state == self.puzzle.goal:
        return path
      elif str(state) not in self.closed:
        self.closed.append(str(state))
        for move in self.puzzle.getNextMove(state):
          if move is not None:
            self.open.put((self.puzzle.heuristic(move), move, path+[move]))
    return None

class AStar:
  def __init__(self, puzzle):
    self.puzzle = puzzle
    self.closed = []
    self.open = PriorityQueue()

  def search(self):
    self.open.put((self.puzzle.heuristic(self.puzzle.initial), self.puzzle.initial, []))
    while not self.open.empty():
      h, state, path = self.open.get()
      if state == self.puzzle.goal:
        return path
      if str(state) not in self.closed:
        self.closed.append(str(state))
        for move in self.puzzle.getNextMove(state):
          if move is not None:
            g = len(path)+1
            h = self.puzzle.heuristic(move)
            self.open.put((g+h, move, path+[move]))
    return None
        
def main():
  initial = [[1,2,3],[4,5,6],[7,0,8]]
  goal = [[1,2,3],[4,5,6],[7,8,0]]
  puzzle = Puzzle(initial, goal)
  puzzle.printState(initial)
  puzzle.printState(goal)
  
  # bfs = BFS(puzzle)
  # path = bfs.search()
  
  # dfs = DFS(puzzle)
  # path = dfs.search()
  
  # dfsl = DFSL(puzzle, 10)
  # path = dfsl.search()
  
  # dfsid = DFSID(puzzle)
  # path = dfsid.search()

  # ucs = UCS(puzzle)
  # path = ucs.search()

  # simpleHillClimb = SimpleHillClimb(puzzle)
  # path = simpleHillClimb.search()

  # bestFirstSearch = BestFirstSearch(puzzle)
  # path = bestFirstSearch.search()

  aStar = AStar(puzzle)
  path = aStar.search()

  if path is None:
    print('No solution found')
  else:
    for state in path:
      puzzle.printState(state)

if __name__ == '__main__':
  main()