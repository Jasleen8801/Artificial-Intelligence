# Lab Assignment 2
# Task 1
# Given two jugs- a 4 litre and 3 litre capacities. Neither has any measurable marker on it. There is a pump which can be used to fill the jugs with water. Simulate the procedure to get exactly 2 litre of water into 4-litre jug.

class Jug:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0

  def fill(self, amount):
    if self.current + amount <= self.capacity:
      self.current += amount
      return True
    return False
  
  def empty(self):
    self.current = 0

  def transfer(self, jug):
    amount = jug.current
    if self.fill(amount):
      jug.empty()
      return True
    return False
  
  def printState(self):
    print(f"Current: {self.current}, Capacity: {self.capacity}")

def main():
  jug3 = Jug(3)
  jug4 = Jug(4)
  jug3.fill(3)
  jug3.transfer(jug4)
  jug3.fill(3)
  jug3.transfer(jug4)
  jug4.fill(4)
  jug4.transfer(jug3)
  jug3.transfer(jug4)
  jug3.fill(3)
  jug3.transfer(jug4)
  jug4.printState()
  jug3.printState()

if __name__ == "__main__":
  main()