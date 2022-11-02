# [BOJ] 2512 예산
"""
1. 합을 구하기는 해야 함
#####
###
2. 예산과 총 합의 차이
3. 상한선을 구하라.
"""
import sys

N = int(input())
budgets = list(map(int, sys.stdin.readline().split()))
budgets.sort()
total = int(input())


def findMax(arr):
    sum = 0
    for num in range(len(arr)):
        if sum+(arr[num]*(len(arr)-num)) > total:
            return (total-sum)//(len(arr)-num)
        sum += arr[num]


upper = max(budgets)
if sum(budgets) > total:
    upper = findMax(budgets)
print(upper)



"""
시간초과
def getTotal(num):
    total = 0
    for budget in budgets:
        if budget <= num:
            total += budget
        else:
            total += num
    return total


upper = max(budgets)
if sum(budgets) > total:
    # total//N < upper < min(total-N, max)
    for i in range(min(total-N, upper), total//N-1, -1):
        if(getTotal(i) <= total):
            upper = i
            break
print(upper)

"""
'''
다른 풀이
n = int(input())
a = list(map(int, input().split()))
k = int(input())
lo = 0
hi = max(a)
while lo <= hi:
    mid = (lo + hi) // 2
    s = 0
    for i in a:
        s += min(i, mid)
    if s <= k:
        lo = mid + 1
    else:
        hi = mid - 1
print(max(0, hi))
'''


