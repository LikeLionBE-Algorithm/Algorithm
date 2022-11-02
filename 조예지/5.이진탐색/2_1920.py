# [BOJ] 1920 수 찾기

import sys
def binary_search(pool, target, start, end):
    if start > end:
        return 0;
    else:
        mid = (start+end)//2
        if pool[mid] == target:
            return 1;
        elif target < pool[mid]:
            return binary_search(pool, target, start, mid-1)
        else:
            return binary_search(pool, target, mid+1, end)


N = int(input())
nums1 = list(map(int, sys.stdin.readline().split()))
nums1.sort()
M = int(input())
nums2 = list(map(int, sys.stdin.readline().split()))

for num in nums2:
    print(binary_search(nums1, num, 0, N-1))





"""
@@@ 시간초과
input()
nums1 = list(map(int, sys.stdin.readline().split()))
M = int(input())
nums2 = list(map(int, sys.stdin.readline().split()))

for num in nums2:
    if num in nums1:
        print(1)
    else:
        print(0)
"""

