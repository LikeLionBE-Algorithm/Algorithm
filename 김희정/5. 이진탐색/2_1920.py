'''
[BOJ] 1920 수 찾기
나의 idea : 이진탐색으로 target 존재 여부 탐색
'''

def binary_search(arr, target, start, end):
    while(start <= end):
        mid = (start+end)//2
        if(arr[mid] > target):
            end = mid - 1
        elif(arr[mid] < target):
            start = mid + 1
        else:
            return mid
    return None
import sys
n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

n_list.sort()
for elem in m_list:
    if binary_search(n_list, elem, 0, n-1) != None:
        print(1)
    else:
        print(0)
