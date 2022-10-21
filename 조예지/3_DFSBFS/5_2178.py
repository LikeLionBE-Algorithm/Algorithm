# 2178 미로탐색
"""
DFS 이용
몇개를 지나갔는지를 알아야 함

못 품!
"""

N, M = map(int, input().split())

graph = []

for i in range(N):
    graph.append(list(input()))


def dfs(r, c, cnt):
    graph[c][r] = "0"
    for i in range(4):
        nc = c + cc[i]
        nr = r + cr[i]
        if nc == (N - 1) and nr == (M - 1):
            result.append(cnt + 1)
            return
        elif 0 <= nc < N and 0 <= nr < M:
            if graph[nc][nr] == "1":
                dfs(nr, nc, cnt + 1)


# 먼저 오른쪽, 아래를 탐색하는 순서도 신경쓰자
cc = [0, 1, -1, 0]
cr = [1, 0, 0, -1]

cnt = 1
result = []


dfs(0, 0, cnt)
print(min(result))
