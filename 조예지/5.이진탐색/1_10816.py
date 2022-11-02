# [BOJ] 10816 숫자 카드 2
"""
중복되는 카드 개수 카운트
카드 숫자의 범위가 너무 넓어서 배열을 패스
1) 딕셔너리 이용
    - 딕셔너리 만들기
        x = {} 또는 y = dict()
    - 기본 모양
        dic = {'name' : 'hoon', 'age' : 4}
    - 추가하기
        dic['weight'] = 7.7
    - 삭제하기
        del dic['weight']
    - key 리스트
        list(dict.keys())
"""


import sys

global SC
SC = dict()

def toDic(inp):
    card = int(inp)
    if SC.get(card) == None:
        SC[card] = 0
    SC[card] += 1


def binary_search(pool, target):
    start = 0
    #그냥 len(pool)로 하니까 IndexError
    end = len(pool)-1
    while start <= end:
        mid = (start+end)//2
        if pool[mid] == target:
            return True
        elif target < pool[mid]:
            end = mid-1
        else:
            start = mid + 1
    return False


N = int(input())
for inp in sys.stdin.readline().split():        #딕셔너리에 입력
    toDic(inp)
M = int(input())
TC = list(map(int, sys.stdin.readline().split()))

cards = sorted(list(SC.keys()))     #키값 리스트로 저장 후 정렬

for num in TC:
    if binary_search(cards, num):
        print(SC[num], end=" ")
    else:
        print(0, end=" ")





