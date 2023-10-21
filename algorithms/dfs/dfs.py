# General DFS for Directed Graph

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

Q = deque()
clock = 0
visited = {}
preorder = {}
parent = {}
for v in graph:
    visited[v] = False
    preorder[v] = 0
    parent[v] = 0
print(visited)
print(preorder)
print(parent)

def explore(clock,Q,visited,preorder,parent):
    while Q:
        v = Q.popleft()
        if not visited[v]:
            visited[v] = True
            preorder[v] = clock + 1
            clock += 1
        for u in graph[v]:
            if not visited[u]:
                parent[u] = v
                Q.append(u)

for v in graph:
    if not visited[v]:
        Q.append(v)
        explore(clock,Q,visited,preorder,parent)
print(visited)
print(preorder)
print(parent)
