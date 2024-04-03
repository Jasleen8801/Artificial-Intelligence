class node:

    def __init__(self,start_node,path,cost):
        self.node=start_node
        self.path=path
        self.cost=cost


def tsp(n):
    open_list=[n]
    closed_list=set()
    min_cost=float('inf')
    min_path=[]
    n=len(graph)
    while open_list:
        current_element=open_list.pop(-1)
        
        if len(current_element.path)==n and graph[current_element.path[-1]][start_node]!=0:
            if (current_element.cost + graph[current_element.path[-1]][start_node])<min_cost:
                min_cost=current_element.cost + graph[current_element.path[-1]][start_node]
                min_path=current_element.path + [start_node]

        else:
            for i in range(n):
                if i not in current_element.path and graph[current_element.node][i]!=0:
                    new_node = i
                    new_path = current_element.path + [i]
                    new_cost = current_element.cost + graph[current_element.node][i]
                    open_list.append(node(new_node, new_path, new_cost))
        
    return min_cost,min_path

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

start_node = 0
n=node(0,[0],0)
min_cost,min_path=tsp(n)
print(min_cost,min_path)