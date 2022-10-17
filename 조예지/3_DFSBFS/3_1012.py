"""
1. 그래프를 어떻게 그릴지
    - 문제 의도상 이차 배열을 원하는 거 같음
2. 진입을 어떻게 카운트 할지
"""
from collections import deque

#test 개수
T = int(input())
for _ in range(T):
    #M: 가로길이, N: 세로길이, K: 배추개수
    M, N, K = map(int, input().split())
    graph = [[] for _ in range(T+1)]

    cbgs = []
    for _ in range(K):
        a, b = map(int, input().split())
        cbgs.append([a, b])

    visited = [False]*K
    queue = deque([])
    cnt = 0
    while True:
        if False in visited:
            queue.append(visited.index(False))
            while (queue):
                target = queue.popleft()
                visited[target] = True
                cx = cbgs[target][0]
                cy = cbgs[target][1]
                nearExp = [[cx + 1, cy], [cx - 1, cy], [cx, cy + 1], [cx, cy - 1]]
                cbgForCheck = [x for x in range(len(cbgs)) if not visited[x]]
                for idx in cbgForCheck:
                    for near in nearExp:
                        if cbgs[idx] == near:
                            visited[idx] = True
                            queue.append(idx)
            cnt += 1
        else:
            break;


    print(cnt)

