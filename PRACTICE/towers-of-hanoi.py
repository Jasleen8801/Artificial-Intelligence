class TowersOfHanoi:
  def __init__(self, towers):
    self.towers = towers

  def getPossMoves(self):
    moves = []
    for i in range(3):
      for j in range(3):
        if i!=j:
          if self.canMove(i, j):
            new_towers = self.move(i,j)
            moves.append(TowersOfHanoi(new_towers))

    return moves
  
  def canMove(self, fromTower, toTower):
    if len(self.towers[fromTower]) == 0: return False
    if len(self.towers[toTower]) == 0: return True
    return self.towers[fromTower][-1] < self.towers[toTower][-1]
  
  def move(self, fromTower, toTower):
    new_towers = [list(tower) for tower in self.towers]
    disk = new_towers[fromTower].pop()
    new_towers[toTower].append(disk)
    return new_towers
  
  def isGoal(self, goal):
    return self.towers[goal] == list(range(len(self.towers[goal]), 0, -1))
  
  def __str__(self) -> str:
    return str(self.towers)

def main():
  initialState = TowersOfHanoi([[3,2,1],[],[]])
  goal = TowersOfHanoi([[],[],[3,2,1]])
  print(initialState)
  print(goal)
  print(initialState.isGoal(2))
  print(initialState.getPossMoves())

if __name__ == "__main__":
  main()