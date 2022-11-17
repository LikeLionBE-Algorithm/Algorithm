'''
[BOJ] 1717 집합의 표현
- 서로소 집합
'''
import sys
sys.setrecursionlimit(10**6)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)
    if  parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

input = sys.stdin.readline
n,m = map(int, input().split())


parent = [0]*(n+1)
for i in range(0,n+1):
    parent[i] = i

for _ in range(m):
    command,a,b = map(int, input().split())
    if(command == 0):
        union_parent(parent, a, b)
    else:
        parent_a = find_parent(parent, a)
        parent_b = find_parent(parent,b)
        #부모 노드가 같으면 같은 집합
        if parent_b == parent_a:
            print("YES")
        else:
            print("NO")