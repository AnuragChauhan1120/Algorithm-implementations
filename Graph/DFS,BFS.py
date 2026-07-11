from collections import defaultdict, deque
#Implementing DFS and BFS for a graph in all ways 

#For graph with n nodes from 0 to n-1 given as edges
n = 6
edges = [[0,1,1],[0,2,3],[1,3,4],[2,4,2],[4,5,1],[1,4,6],[0,5,8]]

graph = defaultdict(list)

for u,v,w in edges:
    graph[u].append(v)           # Considering undirected graph
    graph[v].append(u)

vis = [0]*len(graph)

def dfs(node):
    vis[node] = 1
    print(node)

    for neighbor in graph[node]:
        if vis[neighbor] == 0:
            dfs(neighbor)

for i in range(n):
    if vis[i] == 0:
        dfs(i)

print("dfs done")

vis = [0]*len(graph)

def bfs(node):
    q = deque([node])

    while q:
        j = q.popleft()
        vis[j] = 1
        print(j)

        for neighbor in graph[j]:
            if vis[neighbor] == 0:
                q.append(neighbor)

for i in range(n):
    if vis[i] == 0:
        bfs(i)

