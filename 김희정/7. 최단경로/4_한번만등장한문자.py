'''
[Programmers] 한 번만 등장한 문자
나의 idea : 각 문자 dictionary에 저장 >> count
'''

def solution(s):
    a = dict()
    answer = ""
    #dict초기화
    for i in set(s):
        a[i] = 0

    for elem in s:
        a[elem] += 1
    for key in a.keys():
        if a[key] == 1:
            answer += key
    return ''.join(sorted(answer)) #리스트를 문자열로 변환

'''
other solution : s.count(c) 가능
'''
def solution(s):
    answer = "".join(sorted([ ch for ch in s if s.count(ch) == 1]))
    return answer