graph = {
    'A': ['B', 'C'],
    'B': ['E'],
    'C': ['D'],
    'D': ['A', 'H'],
    'E': ['F', 'G', 'H'],
    'F': ['G', 'B'],
    'G': [],
    'H': ['G'],
}

def find_path(v, t, visited, path, length):
    visited[v] = True
    path[length] = v
    length += 1
    if v == t:
        return True
    for u in graph[v]:
        if not visited[u]:
            if find_path(u, t, visited, path, length):
                return True
    path[length] = None
    length -= 1
    return False

visited = {}
path = [None] * len(graph)
for v in graph:
    visited[v] = False

if find_path('A', 'H', visited, path, 0):
    print("Path found:")
    for node in path: 
        if node is not None:
            print(node,end=' -> ')
else:
    print("Path not found.")
