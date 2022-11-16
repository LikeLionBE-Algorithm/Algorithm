'''
[BOJ] 1916 최소비용 구하기
나의 idea : 특정 도시로 가는 최단경로(버스) 구하기 >> 다익스트라 알고리즘
'''
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input()) #도시의 갯수 - 노드
m = int(input()) #버스의 개수 - 간선

graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
start, end = map(int, input().split())
def dijkstra(start):
    q = [] #(거리, 노드)
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        #이미 처리된 노드
        if distance[now] < dist:
            continue
        for elem in graph[now]:
            cost = dist + elem[1]
            if cost < distance[elem[0]]:
                distance[elem[0]] = cost
                heapq.heappush(q, (cost, elem[0]))
dijkstra(start)
print(distance[end])