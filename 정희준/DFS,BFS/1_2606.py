import sys 

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = []
for k in range(n+1):
    graph.append([])
for l in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (n+1)
count = 0 
def dfs(graph,start,visited):
    global count
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            count+=1
            visited[i] == 1
            dfs(graph,i,visited)

dfs(graph,1,visited)
print(count)

