# [BOJ] 10815 숫자 카드
"""
1. 이진 탐색은 정렬 후 사용
2. 시간 초과
"""

import sys

def bs (arr, target):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start+end)//2        #가운데 점
        if target < arr[mid]:
            end = mid-1
        elif arr[mid] < target:
            start = mid+1
        else:
            return 1 #mid
    return 0 #None


N = int(input())
SC = list(map(int, sys.stdin.readline().split()))
SC.sort()
M = int(input())
TC = list(map(int, sys.stdin.readline().split()))

for cd in TC:
    print(bs(SC, cd), end=" ")
