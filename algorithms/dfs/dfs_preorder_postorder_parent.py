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

clock = 0
visited = {}
preorder = {}
postorder = {}
parent = {}

for v in graph:
    visited[v] = False
    preorder[v] = 0
    postorder[v] = 0
    parent[v] = None

print("Before:")
print(parent)
print(preorder)
print(postorder)

def explore(clock, v, preorder, postorder, parent):
    visited[v] = True
    clock += 1
    preorder[v] = clock

    for u in graph[v]:
        if not visited[u]:
            parent[u] = v
            clock = explore(clock, u, preorder, postorder, parent)

    clock += 1
    postorder[v] = clock
    return clock

for v in graph:
    if not visited[v]:
        clock = explore(clock, v, preorder, postorder, parent)

print("After:")
print(parent)
print(preorder)
print(postorder)
