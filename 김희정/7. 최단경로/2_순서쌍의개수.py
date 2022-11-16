'''
[Programmers] 순서쌍의 개수
나의 idea : n을 1~n까지의 수로 나눴을 때 나눠 떨어지면 count
'''

def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n % i == 0:
            answer += 1
    return answer

if __name__ == '__main__':
    n1 = 20
    print(solution(n1))
    n2 = 100
    print(solution(n2))