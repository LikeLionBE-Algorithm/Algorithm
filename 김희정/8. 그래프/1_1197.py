'''
[BOJ] 1197 최소 스패닝 트리
- 크루스칼 알고리즘 적용
'''
import sys

def find_parent(parent, x):
    #루트 노드 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)
    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b


V,E = map(int, sys.stdin.readline().split())

parent = [0]*(V+1)
edges = []
result = 0

for i in range(V+1):
    parent[i] = i

for _ in range(E):
    a,b,c = map(int, sys.stdin.readline().split())
    edges.append((c,a,b))

edges.sort()

for edge in edges:
    c, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union(parent,a,b)
        result += c
print(result)


