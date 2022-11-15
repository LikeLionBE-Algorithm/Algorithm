INF = int(1e9)
N, D = map(int, input().split())
graph = [{} for _ in range(D+1)]

for _ in range(N):
    S, E, L = map(int, input().split())
    if E-S > L and E <= D:
        if graph[S].get(E) == None or graph[S].get(E) > L:
            graph[S][E] = L


distance = [INF]*(D+1)
distance[0] = 0
for d in range(len(distance)):
    if d != 0:
        distance[d] = min((distance[d-1]+1), distance[d])
    if graph[d] != {}:
        for key in graph[d]:
            new_dist = distance[d] + graph[d].get(key)
            if new_dist < distance[key]:
                distance[key] = new_dist
print(distance[-1])