'''
BOJ_18352_특정 거리의 도시 찾기
나의 idea : BFS를 써 최단거리를 count한다.
- distacne랑 visited 따로 만들기
- python3는 시간초과, pypy3 통과
'''
from collections import deque
import sys

'''
n = 도시 갯수
m = 도로 갯수
k = 거리 정보
x = 출발 도시 번호
'''
n,m,k,x = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
distances = [0]*(n+1) # 각 노드별 최단 거리 저장하는 배열
visited = [False]*(n+1) #각 노드별 방문 여부

queue = deque([x]) #탐색 시작 노드 큐 삽입 후 방문 처리
visited[x] = True
while queue:
    #큐에서 노드 꺼내
    v = queue.popleft()
    # 해당 노드의 인접 노드 중 방문하지 않은 노드 모두 큐 삽입 후 방문 처리
    for elem in graph[v]:
        if not visited[elem]:
            queue.append(elem)
            visited[elem] = True
            distances[elem] = distances[v]+1  #현재 노드 거리값 = 이전 노드 거리값 + 1

#최단거리가 k인 노드만 출력
for index,elem in enumerate(distances):
    if elem == k:
        print(index)
#최단거리가 k인 노드가 하나도 없으면 -1출력
if k not in distances:
    print(-1)
