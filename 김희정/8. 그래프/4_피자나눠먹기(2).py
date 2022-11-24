'''
[Programmers] 피자 나눠 먹기(2)
나의 idea : 6과 n의 최소공배수 구하기
- 6의 배수 중 n과 나눠떨어지는 수 찾기
'''
def solution(n):
    for i in range(1, n + 1):
        if ((6 * i) % n== 0):
            return i


'''
other solution : math라이브러리의 최소공배수 함수(lcm) 사용
>> Python 3.9버전 함수라 프로그래머스에서는 x
'''
import math
def solution(n):
    return  math.lcm(n, 6) // 6