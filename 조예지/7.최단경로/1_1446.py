#[BOJ] 1446 지름길
"""
거점을 저장하기
              --------------
S ---- A ---- B ---- C ---- D
--------------
       ---------------------
"""
import heapq

INF = int(1e9)
N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]
set = {0, D}
#지름길
for _ in range(N):
    S, E, L = map(int, input().split())
    if((E-S) > L) and E <= D:
        set.add(S)
        set.add(E)
        graph[S].append((E, L))
#고속도로 graph 등록
point = sorted(list(set))
k = len(point)
for i in range(k-1):
    graph[point[i]].append((point[i+1], point[i+1]-point[i]))

#최단 거리 테이블 거리값 무한으로 초기화
distance = [INF]*k

def dijkstra():
    q = []
    distance[0] = 0
    heapq.heappush(q, (0, 0))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[point[now]]:
            cost = dist + i[1]
            if cost < distance[point.index(i[0])]:
                distance[point.index(i[0])] = cost
                heapq.heappush(q, (cost, point.index(i[0])))

dijkstra()
print(distance[-1])

