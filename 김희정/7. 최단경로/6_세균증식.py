'''
[Programmers] 세균 증식
나의 idea : 초기 세균 수 * 2^t
'''
def solution(n, t):
    return n * 2**t
if __name__ == '__main__':
    n = 7
    t = 15
    print(solution(n,t))

'''
other solution : 비트 쉬프트 연산 사용
'''
def solution(n, t):
    return n << t