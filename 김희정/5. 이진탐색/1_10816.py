'''
[BOJ] 10816 숫자카드 2
나의 idea : map(dict)사용 : key = target, value=count>> 완전 탐색하면서 해당 target(key) value값 count증가

'''
import sys

n = int(sys.stdin.readline())
sang_cards = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
target_cards = list(map(int,sys.stdin.readline().split()))
sang_cards.sort()
target_dict = dict()
#초기셋팅
for target in target_cards:
    target_dict[target] = 0

for sang in sang_cards:
    if sang in target_dict:
        target_dict[sang] += 1
for t in target_cards:
    print(target_dict.get(t), end=' ')

'''
other solution : 이진 탐색으로 시도 >> '틀렸습니다!'

import sys
def binary_search(arr, target, start, end):
    count = 0
    while start <= end:
        mid = (start + end) // 2
        if(arr[mid]==target):
            count += 1
            startIdx=mid-1
            endIdx=mid+1
            while(startIdx >= 0 and endIdx < len(arr)):
                if arr[endIdx] != target and arr[startIdx] != target:
                    break
                if arr[endIdx] == target:
                    count += 1
                    endIdx += 1

                if arr[startIdx] == target:
                    count += 1
                    startIdx -= 1
            return count
        elif(arr[mid] < target):
            start = mid + 1
        else:
            end = mid - 1
    return count

n = int(sys.stdin.readline())
sang_cards = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
target_cards = list(map(int,sys.stdin.readline().split()))
sang_cards.sort()
result = []

for target in target_cards:
    result.append(binary_search(sang_cards,target,0,n-1))
for elem in result:
    print(elem, end=' ')
'''
