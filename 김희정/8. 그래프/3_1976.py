'''
[BOJ] 1976 여행 가자
나의 idea : 서로소 집합 이용
- 값이 1인 노드들 union 연산
- 여행 경로 붙어 있는 경로끼리 비교
>> parent 같다 == 연결되어있다 == 여행 가능
'''
import sys

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent, a, b):
    parent_a = find_parent(parent,a)
    parent_b = find_parent(parent,b)
    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
parent = [0]*(n+1)
for i in range(1,n+1):
    parent[i] = i

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            if find_parent(parent,i+1) != find_parent(parent,j+1):
                union(parent,i+1,j+1)

#여행 경로 check
travel = list(map(int, sys.stdin.readline().split()))
isTravel = True
for i in range(m-1):
    if parent[travel[i]] != parent[travel[i+1]]:
        isTravel = False
        break
if isTravel:
    print("YES")
else:
    print("NO")
