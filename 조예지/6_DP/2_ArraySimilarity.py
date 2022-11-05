"""
같은 원소의 개수
각각의 원소는 중복된 원소x
"""

def solution(s1, s2):
    answer = 0
    for str in s2:
        if str in s1:
            answer += 1
    return answer


s1 = ["a", "b", "c"]
s2 = ["com", "b", "d", "p", "c"]
print(solution(s1, s2))
s3 = ["n", "omg"]
s4 = ["m", "dot"]
print(solution(s3, s4))