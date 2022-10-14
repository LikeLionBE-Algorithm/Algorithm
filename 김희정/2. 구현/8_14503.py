'''
BOJ_14503_로봇 청소기
나의 idea :
'''

n,m = map(int, input().split())
r,c,d = map(int, input().split())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))
count = 0

#북동남서 : (0,1,2,3)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turnLeft(d):
    if d == 0:
        return 3
    else:
        return d - 1
def turnBack(d):

while True:
    turnCnt = 0
    #1. 현재 위치를 청소한다.
    if grid[r][c] == 0:
        count += 1
        grid[r][c] = 1
        count += 1
    #2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
    #왼쪽 방향에 아직 청소x, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    for _ in range(4):
        nd = turnLeft(d)
        nr = r + dx[d]
        nc = c + dy[d]
        if grid[nr][nc] == 0 :
            r = nr
            c = nc
            d = nd
            break
    if turnCnt == 4:
        if 뒤쪽 벽 :
            break
        else:
            r =

    turnCnt += 1


        if grid[r][c] == 0:
            break



#d%4-1 #왼쪽방향으로 돌리기

print(count)