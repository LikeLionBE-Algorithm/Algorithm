# [Programmers] Level.2 H-Index
"""
h번 이상 인용된 논문이 h편 이상
h의 최대값 = H-Index
"""

def solution(citations):
    answer = -1
    citations.sort(reverse=True)
    for h in range(len(citations)):
        if h+1 == citations[h]:
            answer=h+1
            break
        elif h+1 > citations[h]:
            answer = h
            break
    if answer == -1:
        answer = len(citations)
    return answer

print(solution([3, 0, 6, 1, 5, 7, 4]))
print(solution([7, 6, 5, 4, 3, 1, 0]))
print(solution([10,10,10,1]))
print(solution([100, 100]))

"""
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
    
    
    
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
"""