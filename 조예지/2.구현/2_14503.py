# N:세로크기 M:가로크기
N, M = map(int, input().split())
# (r,c):현재 좌표 d:현재방향
r, c, d = map(int, input().split())

#좌표 상태 저장
cells = []
for i in range(N):
    row = list(map(int, input().split()))
    cells.append(row)

#좌회전 메서드
def turnLeft(s):
    d = (s[2] + 3) % 4
    ns = [s[0], s[1], d]
    return ns

#(좌표, 1) : 앞으로 이동 (좌표, -1) : 뒤로 이동
def move(s, to):
    r = s[0]
    c = s[1]
    d = s[2]
    if d == 0:
        r -= to
    elif d == 1:
        c += to
    elif d == 2:
        r += to
    elif d == 3:
        c -= to
    ns = [r, c, d]
    return ns

#현재 상태 (행, 열, 방향)
state = [r, c, d]
while True:
    sr = state[0]
    sc = state[1]
    # 1. 칸 청소
    cells[sr][sc] = 2

    temp = move(turnLeft(state), 1)
    tr = temp[0]
    tc = temp[1]
    # 2-1. 좌측칸 비었으면 이동
    if cells[tr][tc] == 0:
        state = temp
    # 2-3. 4방향 모두 가지 못하면 후진
    elif (cells[sr - 1][sc] > 0) & (cells[sr + 1][sc] > 0) & (cells[sr][sc - 1] > 0) & (cells[sr][sc + 1] > 0):
        state = move(state, -1)
        # 2-4. 후진 시 벽이면 청소 종료
        if cells[state[0]][state[1]] == 1:
            break
    # 2-2. 좌측칸 청소되어있으면 왼쪽으로 회전
    elif cells[tr][tc] > 0:
        state = turnLeft(state)

# 청소된 칸 수 세기
cnt = 0
for i in range(N):
    for j in range(M):
        if cells[i][j] == 2:
            cnt += 1

print(cnt)

