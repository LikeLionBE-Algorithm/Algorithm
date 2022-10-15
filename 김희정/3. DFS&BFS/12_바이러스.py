'''
BOJ_2606_바이러스
나의 idea : dfs 이용해 연결된 모든 컴퓨터 찾기
'''

def dfs(network, v, visited):
    global cnt
    #현재 노드 방문처리
    visited[v] = True

    for i in network[v]:
        if not visited[i]:
            cnt += 1
            dfs(network,i,visited)

n = int(input()) #컴퓨터 수
pair = int(input()) #컴퓨터 쌍 수
cnt = 0 #바이러스걸린 컴퓨터 수
visited = [False]*(n+1)  #방문처리를 위한 배열
network = [[] for _ in range(n+1)]

#input 배열에 담기
for _ in range(pair):
    u,v = map(int, input().split())
    network[u].append(v)
    network[v].append(u)
dfs(network,1,visited)
print(cnt)