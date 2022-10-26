# [BOJ] 1181 단어 정렬
"""
1. 길이가 짧은 것
2. 길이가 같으면 사전 순으로

set
s = set()
s.add : 요소 하나추가
s.update : 요소 여러개 추가
s.remove
"""
import sys

N = int(input())
arr = [None]*51
for _ in range(N):
    str = sys.stdin.readline().rstrip()
    idx = arr[len(str)]
    if idx == None:
        arr[len(str)] = set()
    arr[len(str)].add(str)

for s in arr:
    if s != None:
        for str in sorted(list(s)):
            print(str)


'''
다른 풀이
n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(sys.stdin.readline().strip())
set_lst = set(lst)
lst = list(set_lst)
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)
'''