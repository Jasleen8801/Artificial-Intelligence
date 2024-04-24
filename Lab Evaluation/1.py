# Lab Evaluation 1 - UCT603
# Name: Jasleen Kaur
# Roll No: 102118064
# Date: 3 April 2024

# 8-puzzle problem with two Empty Blocks.

import copy
from queue import PriorityQueue

class PuzzleNode:
  def __init__(self, state, parent=None, cost=0):
    self.state = state
    self.parent = parent
    self.cost = cost
    self.heuristic = self.calHeuristic()

  def __lt__(self, other):
    return self.heuristic < other.heuristic
  
  def calHeuristic(self):
    # Manhattan Distance
    dis = 0
    for i in range(3):
      for j in range(3):
        if self.state[i][j]!=0:
          dis += abs(i-(self.state[i][j]-1)//3)+abs(j-(self.state[i][j]-1)%3)
    return dis
  
  def isGoal(self):
    return self.state == goal 
  
  def getBlanks(self):
    blanks = []
    for i in range(3):
      for j in range(3):
        if self.state[i][j]==0:
          blanks.append((i,j))
    return blanks
  
  def getSuccessors(self):
    moves = []
    blanks = self.getBlanks()
    for blank in blanks:
      for dir in [(0,1),(0,-1),(1,0),(-1,0)]:
        newx = blank[0]+dir[0]
        newy = blank[1]+dir[1]
        if 0<=newx<3 and 0<=newy<3:
          new_state = copy.deepcopy(self.state)
          new_state[blank[0]][blank[1]] = new_state[newx][newy]
          new_state[newx][newy] = 0
          moves.append(PuzzleNode(new_state, parent=self, cost=self.cost+1))
    return moves
  
  def getPath(self):
    path = []
    curr = self
    while curr is not None:
      path.append(curr.state)
      curr = curr.parent
    return path[::-1]
  
def search(initial):
  vis = set()
  pq = PriorityQueue()
  pq.put(initial)
  while not pq.empty():
    curr = pq.get()
    if curr.isGoal():
      print(f'Total Nodes Expanded: {len(vis)}\n')
      return curr.getPath()
    if str(curr.state) in vis:
      continue
    vis.add(str(curr.state))
    for suc in curr.getSuccessors():
      pq.put(suc)
  return None

initial = [[0, 3, 6], [1, 2, 0], [4, 5, 7]]
goal = [[1, 2, 3], [4, 5, 6], [7, 0, 0]]

initial_node = PuzzleNode(initial)
res = search(initial_node)
if res:
  for state in res:
    for row in state:
      print(row)
    print()
else:
  print("No solution found")

print()
print(f"Cost: {len(res)-1}")