import heapq
import copy

class PuzzleNode:
    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = self.calculate_heuristic()

    def __lt__(self, other):
        return self.cost + self.heuristic < other.cost + other.heuristic

    def calculate_heuristic(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    row_goal, col_goal = divmod(self.state[i][j] - 1, 3)
                    distance += abs(i - row_goal) + abs(j - col_goal)
        return distance

    def is_goal(self):
        return self.state == goal

    def get_successors(self):
        successors = []
        empty_indices = [(i, j) for i in range(3) for j in range(3) if self.state[i][j] == 0]
        for empty_index in empty_indices:
            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_i = empty_index[0] + direction[0]
                new_j = empty_index[1] + direction[1]
                if 0 <= new_i < 3 and 0 <= new_j < 3:
                    new_state = copy.deepcopy(self.state)
                    new_state[empty_index[0]][empty_index[1]] = new_state[new_i][new_j]
                    new_state[new_i][new_j] = 0
                    successors.append(PuzzleNode(new_state, parent=self, cost=self.cost + 1))
        return successors

    def get_path(self):
        path = []
        current = self
        while current is not None:
            path.append(current.state)
            current = current.parent
        return path[::-1]

def best_first_search(initial_state):
    visited = set()
    priority_queue = []
    heapq.heappush(priority_queue, initial_state)

    while priority_queue:
        current_node = heapq.heappop(priority_queue)
        if current_node.is_goal():
            return current_node.get_path()
        visited.add(tuple(map(tuple, current_node.state)))

        for successor in current_node.get_successors():
            if tuple(map(tuple, successor.state)) not in visited:
                heapq.heappush(priority_queue, successor)

    return None

# Define initial and goal states
initial = [[0, 3, 6], [1, 2, 0], [4, 5, 7]]
goal = [[1, 2, 3], [4, 5, 6], [7, 0, 0]]

# Create initial puzzle node
initial_node = PuzzleNode(initial)

# Perform best-first search
solution_path = best_first_search(initial_node)

# Print solution path
if solution_path:
    print("Solution found!")
    for i, state in enumerate(solution_path):
        print(f"Step {i+1}:")
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")
