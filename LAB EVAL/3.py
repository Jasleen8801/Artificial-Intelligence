# Lab Assignment 2
# Task 1: Water Jug Problem

class WaterJug:
  def __init__(self, cap):
    self.cap = cap
    self.current = 0

  def fill(self, amt):
    if self.current+amt<=self.cap:
      self.current += amt
      return True
    return False
  
  def empty(self):
    self.current = 0

  def transfer(self, jug):
    amt = jug.current
    if self.fill(amt):
      jug.empty()
      return True
    return False
  
  def printState(self):
    print(f"Current: {self.current}, Capacity: {self.cap}")

def main():
  jug1 = WaterJug(3)
  jug2 = WaterJug(4)
  jug1.fill(3)
  jug1.transfer(jug2)

if __name__ == "__main__":
  main()