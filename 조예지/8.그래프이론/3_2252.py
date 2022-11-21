#[BOJ] 2252 줄 세우기
from collections import deque

N, M = map(int, input().split())

ind = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    ind[b] += 1


result = []
q = deque()


for i in range(1, N+1):
    if ind[i] == 0:
        q.append(i)


while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
        ind[i] -= 1
        if ind[i] == 0:
            q.append(i)


for r in result:
    print(r, end=" ")
