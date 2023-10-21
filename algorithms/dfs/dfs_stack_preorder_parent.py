# General DFS for Directed Graph
from collections import deque

graph = {
    'A': ['C', 'B'],
    'B': ['E'],
    'C': ['D'],
    'D': ['H', 'A'],
    'E': ['H', 'G', 'F'], 
    'F': ['B', 'G'],
    'G': [],
    'H': ['G'],
}

stack = []
clock = 0
visited = {}
preorder = {}
postorder = {}
parent = {}

for v in graph:
    visited[v] = False
    preorder[v] = 0
    parent[v] = None

print("Before:")
print(visited)
print(preorder)
print(parent)

def explore(clock, stack, visited, preorder, parent):
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            preorder[v] = clock + 1
            clock += 1

        for u in graph[v]:
            if not visited[u]:
                parent[u] = v
                stack.append(u)

for v in graph:
    if not visited[v]:
        stack.append(v)
        explore(clock, stack, visited, preorder, parent)

print("After:")
print(visited)
print(preorder)
print(parent)
