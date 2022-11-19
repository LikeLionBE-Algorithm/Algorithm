'''
[Programmers] 약수 구하기
나의 idea : n을 1부터 n까지 수로 나누기 >> 나눠떨어지는 수 = 약수
'''

def solution(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            answer.append(i)
    return answer
