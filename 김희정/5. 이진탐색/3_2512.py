'''
[BOJ] 2512 예산
나의 idea : 상한액 범위 정하고 그 사이에서 가능한지 검사하고 최대 상한액 찾기 >> 이진탐색으로 시간복잡도 줄이기
1. 상한액 범위 : total//n ~ sum(budget_request)//n 사이에 존재
ex) 485//4 ~ (120+110+140+150)//4
>> 틀림!
반례 :
4
1 1 3 7
11
답 : 6 , 출력 : 4
2. 상한액 범위 : 0 ~ budget요청 중 최댓값
'''
import sys

n = int(sys.stdin.readline()) #지방의 수
budget_request = list(map(int, sys.stdin.readline().split())) #각 지방별 예산요청
total_budget = int(sys.stdin.readline())    #총 예산
budget_request.sort()
result = []
#모든 요청이 배정될 수 있는 경우
if(sum(budget_request) <= total_budget):
    print(max(budget_request))
else:
    start_budget = 0
    end_budget = budget_request[n-1]
    while(start_budget <= end_budget):
        mid = (start_budget + end_budget)//2
        # max_budget을 넘는게 있는지 탐색
        # 안넘으면 그대로 sum에 더하기
        # 넘으면 max값 더하기
        temp_sum = sum(min(req, mid) for req in budget_request)
        if temp_sum > total_budget:
            end_budget = mid - 1
        else:
            result.append(mid)
            start_budget = mid + 1
    print(max(result))
