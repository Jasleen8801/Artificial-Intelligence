from collections import deque

class Knapsack:
  def __init__(self, items, cap):
    self.items = items # list of tuples (value, weight)
    self.cap = cap

  def get_value(self, items):
    '''profit of items in knapsack'''
    val = 0
    for i in items:
      val += i[0]
    return val
  
  def get_weight(self, items):
    '''weight of items in knapsack'''
    weight = 0
    for i in items:
      weight += i[1]
    return weight
  
  def can_add(self, items, item):
    return self.get_weight(items + [item]) <= self.cap
  
  def get_next_moves(self, items):
    moves = []
    for item in self.items:
      if self.can_add(items, item):
        moves.append(items + [item])
    return moves
  
  def is_goal(self, items):
    return self.get_weight(items) == self.cap
  
  def heuristic(self, items):
    return self.get_value(items)
  
class BFS:
  def __init__(self, knapsack):
    self.knapsack = knapsack
    self.closed = []
    self.open = deque()

  def search(self):
    self.open.append([])
    while self.open:
      items = self.open.popleft()
      if self.knapsack.is_goal(items):
        return items
      elif items not in self.closed:
        self.closed.append(items)
        for move in self.knapsack.get_next_moves(items):
          self.open.append(move)
    return None

class DFS:
  def __init__(self, knapsack):
    self.knapsack = knapsack
    self.open = []
    self.closed = []

  def search(self):
    self.open.append([])
    while self.open:
      items = self.open.pop()
      if self.knapsack.is_goal(items):
        return items
      elif items not in self.closed:
        self.closed.append(items)
        for move in self.knapsack.get_next_moves(items):
          self.open.append(move)
    return None

def main():
  items = [(60, 10), (100, 20), (120, 30)]
  cap = 50
  knapsack = Knapsack(items, cap)
  # bfs = BFS(knapsack)
  # items = bfs.search()
  dfs = DFS(knapsack)
  items = dfs.search()
  print(items)
  print(knapsack.get_value(items))

if __name__ == '__main__':
  main()