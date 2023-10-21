# συνάρτηση εύρεσης απογόνων (findchildren) ενος κόμβου

from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['E'],
    'C': ['D'],
    'D': ['A','H'],
    'E': ['F','G','H'],
    'F': ['G','B'],
    'G': [ ] ,
    'H': ['G'] ,
}

def find_children(node, graph):
    queue = deque()
    queue.append(node)
    visited = set()
    children = []

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            visited.add(current_node)
            children.append(current_node)

            for u in graph[current_node]:
                queue.append(u)
    return children

children = find_children('D',graph)
val = range(1,len(children))
print(val)
print("Node",children[0],"has descendants :")
for i in val:
    print(children[i], end=' -> ')