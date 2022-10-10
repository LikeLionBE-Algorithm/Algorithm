'''
BOJ_11945_뜨거운 붕어빵
나의 idea : (1,0) >> (1,M-1), (1,1)>>(1,M-2)
'''

n,m = map(int, input().split())
for _ in range(n):
    line = input()
    s=""
    for i in range(m-1,-1,-1):
        s += line[i]
    print(s)
