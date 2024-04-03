distances = {
    ('A', 'B'): 20,
    ('B', 'A'): 20,
    ('A', 'C'): 42,
    ('C', 'A'): 42,
    ('A', 'D'): 35,
    ('D', 'A'): 35,
    ('B', 'C'): 35,
    ('C', 'B'): 30,
    ('B', 'D'): 34,
    ('D', 'B'): 34,
    ('C', 'D'): 12,
    ('D', 'C'): 12
}

heuristic = {
    'A': 55,
    'B': 45,
    'C': 25,
    'D': 20
}

all_nodes = ['A', 'B', 'C', 'D']

def cal_cost(path):
    cost = 0
    for i in range(len(path)-1):
        cost += distances[(path[i], path[i+1])]
    return cost

def astar(all_nodes):
    rem = all_nodes[1:]
    path = ['A']
    while rem:
        min_cost = float('inf')
        best_node = None
        for node in rem:
            new_path = path + [node]
            cost_so_far = cal_cost(new_path)
            total_cost = cost_so_far + heuristic[node]
            if total_cost < min_cost:
                min_cost = total_cost
                best_node = node
        path.append(best_node)
        rem.remove(best_node)
    path.append(path[0])
    return path

path = astar(all_nodes)
print(path)
print(cal_cost(path))   