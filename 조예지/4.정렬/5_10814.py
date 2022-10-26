# [BOJ] 10814 나이순 정렬

import sys
N = int(input())

mems = [None]*201

for _ in range(N):
    age, name = sys.stdin.readline().rstrip().split()
    if mems[int(age)] == None:
        mems[int(age)] = []
    mems[int(age)].append(name)

for age, names in enumerate(mems):
    if names != None:
        for name in names:
            print(f"{age} {name}")



"""
N = int(sys.stdin.readline())
members = []
for _ in range(N):
    age, name = sys.stdin.readline().split()
    age = int(age)
    members.append([age, name])
members.sort(key=lambda x: x[0])
for i in range(N):
    print(members[i][0], members[i][1])
"""