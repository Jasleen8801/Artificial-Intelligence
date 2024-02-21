# Lab Assignment 3
# Apply Uninformed BFS and DFS search algorithm on 8 puzzle problem.

from assn2_2 import Puzzle
import copy

def DepthFirstSearch(p1):
  open_stack = []
  closed_stack = []
  open_stack.append(p1)
  while open_stack!=[]:
    current = open_stack.pop()
    # current = open_stack.pop(0) queue - BFS
    closed_stack.append(current)
    current.printState(current.current_state)
    if current.isGoalReached():
      print("Goal reached")
      return
    else:
      new_state = copy.deepcopy(current)
      if new_state.moveUp() != None and not checkClosedList(closed_stack, new_state):
        open_stack.append(new_state) 
        new_state.parent = current
      else:
        del new_state
      new_state = copy.deepcopy(current)
      if new_state.moveDown() != None and not checkClosedList(closed_stack, new_state):
        open_stack.append(new_state) 
        new_state.parent = current
      else:
        del new_state
      new_state = copy.deepcopy(current)
      if new_state.moveLeft() != None and not checkClosedList(closed_stack, new_state):
        open_stack.append(new_state) 
        new_state.parent = current
      else:
        del new_state
      new_state = copy.deepcopy(current)
      if new_state.moveRight() != None and not checkClosedList(closed_stack, new_state):
        open_stack.append(new_state) 
        new_state.parent = current
      else:
        del new_state
  print("Goal not reached")
  return

def checkClosedList(closed_stack, new_state):
  for i in range(len(closed_stack)):
    if closed_stack[i].current_state == new_state.current_state:
      return True
  return False

def main():
  my_list = [[2,8,1], [0,4,3], [7,6,5]]
  goal_list = [[1,2,3], [4,5,6], [7,8,9]]
  p1 = Puzzle(my_list, goal_list)
  DepthFirstSearch(p1)
  return

if __name__ == "__main__":
  main()