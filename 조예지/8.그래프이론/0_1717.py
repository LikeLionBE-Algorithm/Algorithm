#[BOJ] 1717 집합의 표현
"""
1. 시간 초과
>> sys 사용, pypy3로 제출
2. 6과 7을 합치고, 3과 7을 합쳤는데 6은 6을 향하고 있다.
[0, 1, 2, 1, 4, 5, 6, 6]
[0, 1, 2, 1, 4, 5, 6, 1]
>>알고리즘을 잘못짬
3. recursion error
parent도 매개변수로 줘야하는데 안 줌
4. 이번엔 6만 1을 향하고 7은 여전히 6을 향한다
[0, 1, 2, 1, 4, 5, 6, 6]
[0, 1, 2, 1, 4, 5, 1, 6]

sys.setrecursionlimit(10**6)
"""

import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
#자기 자신을 부모로 초기화
parent = list(range(0, n+1))

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

def find(a, b):
    return find_parent(a) == find_parent(b)


#함수 실행
for _ in range(m):
    c, a, b = map(int, sys.stdin.readline().split())
    if(c == 0):
        union(a, b)
    else:
        if find(a, b):
            print("YES")
        else:
            print("NO")