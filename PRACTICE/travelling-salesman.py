from itertools import permutations

class TSPState:
  def __init__(self, tour, vis, graph):
    self.tour = tour # current tour
    self.vis = vis # visited nodes
    self.graph = graph 

  def isComplete(self):
    return len(self.tour) == len(self.graph)
  
  def getLastCity(self):
    return self.tour[-1] if len(self.tour) > 0 else None
  
  def getNextCities(self):
    last_city = self.getLastCity()
    if last_city is None:
      return range(len(self.graph)) 
    return [i for i in range(len(self.graph)) if i not in self.vis]
  
  def addCity(self, city):
    new_tour = self.tour + [city]
    new_vis = self.vis + [city]
    return TSPState(new_tour, new_vis, self.graph)
  
def TSP(graph, s):
  initialState = TSPState([s], [s], graph) # start from city s
  minPath = float('inf')

  nextPermutations = permutations(initialState.getNextCities())

  for i in nextPermutations:
    curr_wt = 0
    prev = s
    for j in i:
      curr_wt += graph[prev][j]
      prev = j
    curr_wt += graph[prev][s]
    minPath = min(minPath, curr_wt)

  return minPath

def main():
  graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
  s = 0
  print(TSP(graph, s))

if __name__ == "__main__":
  main()