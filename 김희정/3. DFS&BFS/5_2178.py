'''
BOJ_2178_미로탐색
나의 idea : bfs로 인접한 칸 탐색, 이동 칸 수를 grid에 저장하면서 진행
[input]
4 6
101111
101010
101011
111011
[output]
3, 0, 9, 10, 11, 12
2, 0, 8, 0, 12, 0
3, 0, 7, 0, 13, 14
4, 5, 6, 0, 14, 15
15
'''
from collections import deque

n,m = map(int, input().split())
grid = []
for i in range(n):
    grid.append(list(map(int,input())))
#bfs
dx = [-1,1,0,0]
dy = [0,0,1,-1]
queue = deque([(0,0)])
grid[0][0] = 1
while queue:
    #현재 좌표 큐에서 꺼내기
    x,y = queue.popleft()
    #인접 칸 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #범위 넘어가면 pass
        if nx < 0 or nx >=n or ny < 0 or ny >= m:
            continue
        if grid[nx][ny] == 1:
            queue.append((nx,ny))
            grid[nx][ny] = grid[x][y]+1 #현재 진행 칸 수 저장
# print(grid)
print(grid[n-1][m-1])