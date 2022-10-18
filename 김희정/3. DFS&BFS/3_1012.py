'''
BOJ_1012_유기농 배추
나의 idea : 1이 모여 있는 영역 구하기 >> 상하좌우 dfs
- 1. 상하좌우 보고 값이 '1' 이면서 아직 방문 x >> 방문
- 2. 방문 지점 다시 상하좌우 보기
'''
#최대 재귀 깊이를 1,000,000 정도로 설정
#안하면 RecursionError 발생
import sys
sys.setrecursionlimit(10**6)

def dfs(grid,x,y):
    #범위 벗어나면 종료
    if x < 0 or x >= m or y < 0 or y >= n:
        return False

    if grid[x][y] == 1:
        grid[x][y] = 0 #방문 처리
        #상하좌우
        dfs(grid, x-1,y)
        dfs(grid, x+1,y)
        dfs(grid, x, y-1)
        dfs(grid, x, y+1)
        return True
    return False

T = int(input()) #테스트 케이스 갯수
for _ in range(T):
    #input 받기
    m,n,k = map(int,input().split()) # m : 가로길이(x), n : 세로길이(y), k : 심어진 배추 위치 갯수
    grid = [[0]*n for _ in range(m)]
    for _ in range(k):
        x,y = map(int, input().split())
        grid[x][y] = 1
    #dfs 수행
    result = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                continue
            #현재 위치 dfs 탐색
            if dfs(grid,i,j) == True:
                result += 1
    print(result)

