# [BOJ] 11403 경로 찾기
"""
0 1 0
0 0 1
1 0 0

dfs로 품
"""
from collections import deque

N = int(input())
graph = []
for i in range(N):
    row = list(map(int, input().split()))
    graph.append(row)


visited = [0]*N
for i in range(N):
    queue = deque()
    queue.append(i)
    while queue:
        q = queue.popleft()
        for j in range(N):
            if graph[q][j] == 1 and visited[j] == 0:
                queue.append(j)
                visited[j] = 1
    for k in range(N):
        print(visited[k], end=" ")
    print()
    visited = [0] * N


"""
# 경로 찾기
N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1
for i in graph:
    print(*i)
    
1 > 8 > 9 > 5
"""