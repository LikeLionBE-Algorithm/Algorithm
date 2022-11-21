#[BOJ] 1976 여행 가자
"""
그래프 자료 구조로 parents 리스트 만들기??
"""


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())
M = int(input())


parent = [0] * (N+1)
for i in range(N):
    parent[i] = i


for i in range(N):
    row = list(map(int, input().split()))
    for j in range(i, N):
        if row[j] == 1:
            union(i+1, j+1)



cities = list(set(map(int, input().split())))


result = set(list(map(lambda x : find_parent(x), cities)))

if len(result) == 1:
    print("YES")
else:
    print("NO")
