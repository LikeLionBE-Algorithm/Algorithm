'''
[Programmers] 배열의 유사도
나의 idea : 배열의 길이가 길지 않으므로(<=100) 완전탐색으로 해결
'''

def solution(s1, s2):
    answer = 0
    for elem in s1:
        for elem2 in s2:
            if(elem==elem2):
                answer += 1
    return answer

'''
other solution : 교집합 이용
'''
def solution(s1, s2):
    return len(set(s1)&set(s2));
