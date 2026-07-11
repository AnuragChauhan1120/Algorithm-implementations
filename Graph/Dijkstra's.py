from collections import defaultdict, deque
import heapq

#Implementing Dijkstra's algorithm to find shortest path for all nodes from a particular node

edges = [[0,1,1],[0,2,3],[1,3,4],[2,4,2],[4,5,1],[1,4,6],[0,5,8]]


graph = defaultdict(list)
for u,v,w in edges:
    graph[u].append([w,v])
    graph[v].append([w,u])

distances = [float('inf')]*len(graph)

start = 0    # Taking 0 as the starting point, to find the min. distance from
distances[start] = 0

pq = []
heapq.heappush(pq, (0,start)) 
# input = (list, (distance,node)); (distance, node) to prioritise distance based sorting in heap

while pq:
    distance, node = heapq.heappop(pq)

    if distance > distances[node]:         # If already smaller path present, then continue
        continue

    for weight, neighbor in graph[node]:
        d = weight+distance

        if d < distances[neighbor]:
            distances[neighbor] = d
            heapq.heappush(pq, (d,neighbor))


print(distances)
