'''
Programmers : level1 모의고사
나의 idea : 각각 케이스 하나씩 다 돌면서 count
'''


def solution(answers):
    answer = []
    answer_len = len(answers)

    p1_answer = [1,2,3,4,5]*(answer_len//5+1)
    p2_answer = [2,1,2,3,2,4,2,5]*(answer_len//8+1)
    p3_answer = [3,3,1,1,2,2,4,4,5,5]*(answer_len//10+1)

    result = [0,0,0] #정답 갯수 count

    for i in range(answer_len):
        if answers[i] == p1_answer[i]:
            result[0] += 1
        if answers[i] == p2_answer[i]:
            result[1] += 1
        if answers[i] == p3_answer[i]:
            result[2] += 1

    #가장 많이 맞춘 사람 리턴
    #동률도 추가
    max_value = max(result)
    for i in range(3):
        if result[i] == max_value:
            answer.append(i+1)

    return answer

if __name__ == '__main__':
    print(solution([1,2,3,4,5]))

'''
[other solution]
- 길이 넘어가는 경우 처리하는 법 : idx%len(pattern1)
- for idx, s in enumerate(list) : 배열의 원소값과 인덱스 둘 다 사용 
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

'''