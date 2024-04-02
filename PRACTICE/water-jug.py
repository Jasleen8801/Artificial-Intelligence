import copy

class Jug:
  def __init__(self, cap) -> None:
    self.cap = cap
    self.curr = 0

  def fill(self, amt):
    if self.curr+amt<=self.cap:
      self.curr += amt
      return True
    return False
  
  def empty(self):
    self.curr = 0

  def transfer(self, jug):
    if self.fill(jug.curr):
      jug.empty()
      return True
    return False
  
  def printState(self):
    print(f"Curr: {self.curr}, Cap: {self.cap}")


def getNextMove(jug1, jug2):
  moves = []

  if jug1.curr<jug1.cap:
    new_jug1 = copy.deepcopy(jug1)
    new_jug1.fill(jug1.cap-jug1.curr)
    moves.append((new_jug1, jug2))

  if jug2.curr<jug2.cap:
    new_jug2 = copy.deepcopy(jug2)
    new_jug2.fill(jug2.cap-jug2.curr)
    moves.append((jug1, new_jug2))

  if jug1.curr>0:
    new_jug1 = copy.deepcopy(jug1)
    new_jug1.empty()
    moves.append((new_jug1, jug2))

  if jug2.curr>0:
    new_jug2 = copy.deepcopy(jug2)
    new_jug2.empty()
    moves.append((jug1, new_jug2))

  if jug1.curr>0 and jug2.curr<jug2.cap:
    new_jug1 = copy.deepcopy(jug1)
    new_jug2 = copy.deepcopy(jug2)
    new_jug1.transfer(new_jug2)
    moves.append((new_jug1, new_jug2))

  if jug2.curr>0 and jug1.curr<jug1.cap:
    new_jug1 = copy.deepcopy(jug1)
    new_jug2 = copy.deepcopy(jug2)
    new_jug2.transfer(new_jug1)
    moves.append((new_jug1, new_jug2))

  return moves

