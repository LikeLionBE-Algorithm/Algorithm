#[BOJ] 1916 최소비용 구하기
"""
다익스트라
"""
import heapq
import sys

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    S, E, C = map(int, sys.stdin.readline().split())
    graph[S].append((E, C))

start, end = map(int, input().split())

INF = int(1e9)
costs = [INF] * (N+1)

def dijkstra():
    q = []
    heapq.heappush(q, (start, 0))
    while q:
        now, cost = heapq.heappop(q)
        if costs[now] < cost:
            continue
        for i in graph[now]:
            new_cost = cost + i[1]
            if costs[i[0]] > new_cost:
                costs[i[0]] = new_cost
                heapq.heappush(q, (i[0], new_cost))

dijkstra()

print(costs[end])

