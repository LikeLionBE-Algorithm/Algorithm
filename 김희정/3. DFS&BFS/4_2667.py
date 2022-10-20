'''
BOJ_2667_단지번호붙이기
나의 idea : 상하좌우 dfs
- 방문한 곳은 0으로 바꾸기
1. 상하좌우 보고 값이 '1'이면서 아직 방문 x >> 방문
2. 방문 지점 다시 상하좌우
'''

def dfs(grid, x,y):
    global cnt
    #범위 벗어나면 종료
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if grid[x][y] == 1:
        grid[x][y] = 0 #방문처리
        cnt += 1
        #상하좌우
        dfs(grid,x-1,y)
        dfs(grid,x+1,y)
        dfs(grid,x,y-1)
        dfs(grid,x,y+1)
        return True
    return False

if __name__ == '__main__':
    n = int(input()) #지도의 크기(NXN)
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input())))
    sum = 0
    counts = []
    #모든 좌표 탐색
    for i in range(n):
        for j in range(n):
            cnt = 0
            if dfs(grid,i,j) == True:
                sum += 1
                counts.append(cnt)
    print(sum)
    counts.sort()
    for elem in counts:
        print(elem)
