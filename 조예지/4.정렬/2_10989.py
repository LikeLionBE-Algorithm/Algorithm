# [BOJ] 10989 수 정렬하기3
"""
N이 천만개
시간 제한 : 5초
메모리 제한 8MB

1. priorityqueue : 메모리초과
2. 파이썬 라이브러리 정렬 : 메모리초과
3. 계수 정렬 :
    - 데이터의 범위가 한정되고,
    - 더 빠르고,
    - 모든 데이터가 양의 정수
    - 가장 큰 데이터와 작은 데이터의 차이가 1,000,000보다 작을 때
    - 시간 복잡도 O(N+K)
"""
import sys

N = int(sys.stdin.readline())
arr = [0]*10001
max = 0
for _ in range(N):
    n = int(sys.stdin.readline())
    arr[n] += 1
    if max < n:
        max = n

for i in range(max+1):
    for j in range(arr[i]):
        print(i)





"""
1.
import sys
from queue import PriorityQueue

que = PriorityQueue(10000000)

N = int(sys.stdin.readline())
for _ in range(N):
    que.put(int(sys.stdin.readline()))

while not que.empty():
    print(que.get())
"""
