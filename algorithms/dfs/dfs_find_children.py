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

visited = {}
for v in graph:
    visited[v] = False

def find_children(node, graph):
    stack = [node]
    children = []

    while stack:
        current_node = stack.pop()
        if not visited[current_node]:
            visited[current_node] = True
            children.append(current_node)

            for u in graph[current_node]:
                stack.append(u)
    return children

children = find_children('D',graph)
val = range(1,len(children))
print(val)
print("Node",children[0],"has descendants :")
for i in val:
    print(children[i], end=' -> ')