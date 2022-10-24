"""
BFS
단지 내 집의 수 카운트
"""
from collections import deque

N = int(input())
map = []
for _ in range(N):
    line = list(input())
    map.append(line)

cx = [0, 0, -1, 1]
cy = [-1, 1, 0, 0]

def bfs (b, a):
    cnt = 1
    queue = deque([(b,a)])
    while queue:
        target = queue.popleft()
        for i in range(4):
            nx = target[1] + cx[i]
            ny = target[0] + cy[i]
            if (0<=nx<N) and (0<=ny<N) and (map[ny][nx] == '1'):
                map[ny][nx] = '0'
                queue.append((ny, nx))
                cnt += 1
    return cnt

result = []
for y in range(N):
    for x in range(N):
        if map[y][x] == '1':
            map[y][x] = '0'
            cnt = bfs (y, x)
            result.append(cnt)

print(len(result))
result.sort()
for r in result:
    print(r)

"""
1) 그래프 그리는 법
N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().rstrip())))

2) DFS로 풀이
def DFS(x,y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True
    return False

for i in range(N):
    for j in range(N):
        if DFS(i,j) == True:
            num.append(count)
            result += 1
            count = 0



"""


