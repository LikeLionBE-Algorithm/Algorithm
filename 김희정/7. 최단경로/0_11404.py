'''
[BOJ] 11404 플로이드
'''
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0
#간선 정보
for _ in range(m):
    a,b,c = map(int, input().split())
    #노선 중복될 때, 가장 짧은 노선만 고려
    if c < graph[a][b]:
        graph[a][b] = c

#플로이드
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

#결과
for a in range(1,n+1):
    for b in range(1,n+1):
        #갈 수 없는 경우 0출력
        if graph[a][b] == INF:
            print(0,end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
