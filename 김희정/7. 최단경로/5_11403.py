'''
[BOJ] 11403 경로 찾기
나의 idea : 플로이드 워셜 응용
- 그래프 전체 순회하면서 a->b 경로 중, a->k->b 경로가 있는지 확인
- graph[a][k] == 1 and graph[k][b] == 1 >> graph[a][k] and graph[k][b] 리팩토링
    - 파이썬에서 1은 참
'''
import sys
input = sys.stdin.readline
n = int(input()) #정점의 개수
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][k] and graph[k][b]:
                graph[a][b] = 1

for a in range(n):
    for b in range(n):
        print(graph[a][b], end=" ")
    print()