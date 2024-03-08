from heapq import heappush, heappop

class Node:
  def __init__(self, state, parent, g_score, h_score):
    self.state = state
    self.parent = parent
    self.g_score = g_score
    self.h_score = h_score
    self.f_score = g_score + h_score

  def __lt__(self, other):
    return self.f_score < other.f_score

def manhattan_distance(state, goal_state):
  distance = 0
  for i in range(len(state)):
    if state[i] != goal_state[i]:
      row1, col1 = divmod(i, 3)
      row2, col2 = divmod(goal_state.index(state[i]), 3)
      distance += abs(row1 - row2) + abs(col1 - col2)
  return distance

def generate_successors(state):
  successors = []
  blank_index = state.index(0)
  movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  for move in movements:
    new_row, new_col = blank_index // 3 + move[0], blank_index % 3 + move[1]
    if 0 <= new_row < 3 and 0 <= new_col < 3:
      new_state = list(state)
      new_state[blank_index], new_state[new_row * 3 + new_col] = new_state[new_row * 3 + new_col], new_state[blank_index]
      successors.append(new_state)
  return successors

def a_star_search(start_state, goal_state):
  open_list = [Node(start_state, None, 0, manhattan_distance(start_state, goal_state))]
  closed_list = set()

  while open_list:
    current_node = heappop(open_list)

    if current_node.state == goal_state:
      path = []
      while current_node:
        path.append(current_node.state)
        current_node = current_node.parent
      return path[::-1]

    closed_list.add(tuple(current_node.state))

    for successor in generate_successors(current_node.state):
      if tuple(successor) not in closed_list:
        tentative_g_score = current_node.g_score + 1
        new_node = Node(successor, current_node, tentative_g_score, manhattan_distance(successor, goal_state))

        for open_node in open_list:
          if open_node.state == new_node.state and open_node.f_score <= new_node.f_score:
            break
        else:
          heappush(open_list, new_node)

  return None

# Example usage
start_state = [1, 2, 3, 4, 0, 6, 7, 8, 5]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

solution = a_star_search(start_state, goal_state)

if solution:
  print("Solution found!")
  for state in solution:
    print(state)
else:
  print("No solution found.")
