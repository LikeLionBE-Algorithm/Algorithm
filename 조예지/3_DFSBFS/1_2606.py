N = int(input())
M = int(input())

def dfs (graph, infected, i):
    infected[i] = True
    for com in graph[i]:
        if not infected[com] :
            dfs(graph, infected, com)


# graph 만들기
# graph = [[]]*(N+1) : 이렇게 했다가 graph 안의 값들이 동기화 됨
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    # 아래 코드 없어서 반대로 상황은 체크가 안 됨
    graph[b].append(a)



infected = [False]*(N+1)
dfs(graph, infected, 1)


print(infected.count(True)-1)