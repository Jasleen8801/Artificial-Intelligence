# Lab Assignment 5
# Task 1: A* Algorithm

import copy
from queue import PriorityQueue

class EightPuzzle:
  def __init__(self, initial, goal):
    self.initial = initial
    self.goal = goal
  
  def getBlankSpace(self, state):
    for i in range(3):
      for j in range(3):
        if state[i][j]==0:
          return (i,j)
  
  def getHeuristic(self, state):
    cnt = 0
    for i in range(3):
      for j in range(3):
        if state[i][j] == self.goal[i][j]:
          cnt += 1
    return cnt
  
  def getNextMove(self, state):
    blank = self.getBlankSpace(state)
    moves = []

    if blank[1]>0:
      new_state = copy.deepcopy(state)
      new_state[blank[0]][blank[1]] = new_state[blank[0]][blank[1]-1]
      new_state[blank[0]][blank[1]-1] = 0
      moves.append(new_state)

    if blank[1]<2:
      new_state = copy.deepcopy(state)
      new_state[blank[0]][blank[1]] = new_state[blank[0]][blank[1]+1]
      new_state[blank[0]][blank[1]+1] = 0
      moves.append(new_state)

    if blank[0]>0:
      new_state = copy.deepcopy(state)
      new_state[blank[0]][blank[1]] = new_state[blank[0]-1][blank[1]]
      new_state[blank[0]-1][blank[1]] = 0
      moves.append(new_state)

    if blank[0]<2:
      new_state = copy.deepcopy(state)
      new_state[blank[0]][blank[1]] = new_state[blank[0]+1][blank[1]]
      new_state[blank[0]+1][blank[1]] = 0
      moves.append(new_state)

    return moves
  
class AStar:
  def __init__(self, puzzle):
    self.puzzle = puzzle
    self.closed = []
    self.open = PriorityQueue()
    
  def search(self):
    self.open.put((self.puzzle.getHeuristic(self.puzzle.initial), self.puzzle.initial, []))
    while not self.open.empty():
      h, state, path = self.open.get()
      if state == self.puzzle.goal:
        return path
      if str(state) not in self.closed:
        self.closed.append(str(state))
        for move in self.puzzle.getNextMove(state):
          if move is not None:
            g = len(path)+1
            h = self.puzzle.getHeuristic(move)
            f = g+h
            self.open.put((f, move, path+[move]))
    return None
  
def main():
  initial = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
  goal = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

  puzzle = EightPuzzle(initial, goal)
  aStar = AStar(puzzle)

  path = aStar.search()

  print("Initial State:")
  for row in initial:
    print(row)
  print("\nGoal State:")
  for row in goal:
    print(row)
  print("\nPath:")
  for state in path:
    for row in state:
      print(row)
    print()

if __name__ == "__main__":
  main()
