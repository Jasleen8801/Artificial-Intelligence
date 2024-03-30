# Lab Assignment 4
# Task 1: Hill Climbing Algorithm

import copy
import random

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
  
class HillClimbSearch:
  def __init__(self, puzzle):
    self.puzzle = puzzle

  def search(self):
    curr = self.puzzle.initial
    path = [curr]

    while True:
      h = self.puzzle.getHeuristic(curr)
      if h==9: # goal state
        return path
      
      moves = self.puzzle.getNextMove(curr)
      h_next = [self.puzzle.getHeuristic(move) for move in moves]

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

def main():
  initial = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
  goal = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

  puzzle = EightPuzzle(initial, goal)
  hillClimb = HillClimbSearch(puzzle)

  path = hillClimb.search()

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
