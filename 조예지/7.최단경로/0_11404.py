# [BOJ] 11404 플로이드

#도시개수
n = int(input())
#버스노선개수
m = int(input())

#10억
INF = int(1e9)
#2차원 그래프, 모든 값을 INF로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

#자기자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    graph[a][a] = 0

#간선의 정볼를 받아 값을 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    #더 작은 값으로 넣기
    graph[a][b] = min(c, graph[a][b])

#플루이드 워셜 알고리즘
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

#출력
for a in range(1, n+1):
    for b in range(1, n+1):
        val = graph[a][b]
        if val == INF:
            print(0, end=" ")
        else:
            print(val, end=" ")
    print()

