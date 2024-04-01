# Lab Assignment 2
# Task 1: Water Jug Problem

import copy

class WaterJug:
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

  # Fill jug1
  if jug1.curr < jug1.cap:
    next_jug1 = copy.deepcopy(jug1)
    next_jug1.fill(jug1.cap - jug1.curr)
    moves.append((next_jug1, jug2))

  # Fill jug2
  if jug2.curr < jug2.cap:
    next_jug2 = copy.deepcopy(jug2)
    next_jug2.fill(jug2.cap - jug2.curr)
    moves.append((jug1, next_jug2))

  # Empty jug1
  if jug1.curr > 0:
    next_jug1 = copy.deepcopy(jug1)
    next_jug1.empty()
    moves.append((next_jug1, jug2))

  # Empty jug2
  if jug2.curr > 0:
    next_jug2 = copy.deepcopy(jug2)
    next_jug2.empty()
    moves.append((jug1, next_jug2))

  # Transfer jug1 to jug2
  if jug1.curr > 0 and jug2.curr < jug2.cap:
    next_jug1 = copy.deepcopy(jug1)
    next_jug2 = copy.deepcopy(jug2)
    next_jug1.transfer(next_jug2)
    moves.append((next_jug1, next_jug2))

  # Transfer jug2 to jug1
  if jug2.curr > 0 and jug1.curr < jug1.cap:
    next_jug1 = copy.deepcopy(jug1)
    next_jug2 = copy.deepcopy(jug2)
    next_jug2.transfer(next_jug1)
    moves.append((next_jug1, next_jug2))

  return moves

def main():
  jug1 = WaterJug(3)
  jug2 = WaterJug(4)
  jug1.printState()
  jug2.printState()
  jug1.fill(3)
  jug1.printState()
  # jug1.transfer(jug2)
  jug2.transfer(jug1)
  jug1.printState()
  jug2.printState()

if __name__ == '__main__':
  main()