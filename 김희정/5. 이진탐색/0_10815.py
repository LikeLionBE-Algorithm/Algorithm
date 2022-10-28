'''
[BOJ] 10815 숫자카드
나의 idea : 이진 탐색으로 target 카드 존재 여부 판단

'''
import sys

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] < target:
            start = mid +1
        elif arr[mid] > target:
            end = mid -1
        else:
            return mid
    return None

n = int(sys.stdin.readline()) #상근이가 갖고 있는 카드 갯수
sang_cards = list(map(int, input().split()))
sang_cards.sort()
m = int(sys.stdin.readline()) #target 카드 갯수
target_cards = list(map(int, input().split()))

result = []
for target in target_cards:
    value = binary_search(sang_cards,target, 0,n-1)
    if value==None:
        result.append(0)
    else:
        result.append(1)
for elem in result:
    print(elem, end=" ")
