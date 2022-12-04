'''
[BOJ] 2252 줄 세우기
나의 idea : 선후관계가 있으므로 위상 정렬 알고리즘 적용
'''
import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    #큐에서 빠져나간 순서 >> 위상 정렬 수행 결과
    result = []
    q = deque()
    #진입 차수가 0인 노드 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    #큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        result.append(now)
        #해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end=' ')
topology_sort()



