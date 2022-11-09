'''
[Programmers] 모음 제거
나의 idea : in 키워드 사용, 모음 리스트 안에 해당 문자 있으면 빈 문자열로 치환
'''
vowel = ['a', 'e', 'i', 'o', 'u']
def solution(my_string):
    answer = ''
    for elem in my_string:
        if elem in vowel:
            answer += ""
            continue;
        answer += elem
    return answer
