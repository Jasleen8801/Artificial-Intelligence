from queue import Queue

class NQueen:
  def __init__(self, n):
    self.n = n
    self.board = [0]*n
    self.solutions = []

  def putQueen(self, row, col):
    for i in range(row):
      if self.board[i] == col or abs(self.board[i]-col) == row-i or self.board[i] == row:
        return False
    return True
  
  def printSolutions(self):
    for solution in self.solutions:
      print(f'[{", ".join(str(x) for x in solution)}]')
    return
  
  def bfs(self, row):
    oq = Queue()
    cq = Queue()
    oq.put(row)
    while not oq.empty():
      current = oq.get()
      if current == self.n-1:
        self.solutions.append(self.board[:])
      else:
        for col in range(self.n):
          if self.putQueen(current, col):
            self.board[current] = col
            cq.put(current+1)
      if oq.empty():
        oq = cq
        cq = Queue()
    return
  
  def solve(self):
    self.bfs(0)
    return
  
def main():
  n = 4
  q1 = NQueen(n)
  q1.solve()
  q1.printSolutions()
  return

if __name__ == "__main__":
  main()