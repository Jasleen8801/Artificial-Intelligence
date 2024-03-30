# Lab Assignment 3
# Task 1: Breadth First Search 8 Puzzle Problem

import copy
from collections import deque

class EightPuzzle:
  def __init__(self, initial_state, goal_state):
    self.initial_state = initial_state
    self.goal_state = goal_state

  def get_blank_space(self, state):
    for i in range(3):
      for j in range(3):
        if state[i][j] == 0:
          return (i, j)

  def get_next_moves(self, state):
    blank = self.get_blank_space(state)
    moves = []

    if blank[1] > 0:
      # move left
      new_state = copy.deepcopy(state)
      new_state[blank[0]][blank[1]] = new_state[blank[0]][blank[1] - 1]
      new_state[blank[0]][blank[1] - 1] = 0
      moves.append(new_state)

    if blank[1] < 2:
      # move right
      new_state = copy.deepcopy(state)
      new_state[blank[0]][blank[1]] = new_state[blank[0]][blank[1] + 1]
      new_state[blank[0]][blank[1] + 1] = 0
      moves.append(new_state)

    if blank[0] > 0:
      # move top
      new_state = copy.deepcopy(state)
      new_state[blank[0]][blank[1]] = new_state[blank[0] - 1][blank[1]]
      new_state[blank[0] - 1][blank[1]] = 0
      moves.append(new_state)

    if blank[0] < 2:
      # move bottom
      new_state = copy.deepcopy(state)
      new_state[blank[0]][blank[1]] = new_state[blank[0] + 1][blank[1]]
      new_state[blank[0] + 1][blank[1]] = 0
      moves.append(new_state)

    return moves

class BreadthFirstSearch:
  def __init__(self, puzzle) -> None:
    self.puzzle = puzzle
    self.closed = []
    self.open = deque()

  def search(self):
    self.open.append((self.puzzle.initial_state, []))

    while self.open:
      state,path = self.open.popleft()
      if state==self.puzzle.goal_state:
        return path
      elif str(state) not in self.closed:
        self.closed.append(str(state))
        for move in self.puzzle.get_next_moves(state):
          if move is not None:
            self.open.append((move, path+[move]))

    return None

def main():
  initial = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
  goal = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

  puzzle = EightPuzzle(initial, goal)
  bfs = BreadthFirstSearch(puzzle)

  path = bfs.search()

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
