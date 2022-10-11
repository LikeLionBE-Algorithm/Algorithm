# 찍는 방식 구현
# 1번 : (1~5) 반복
def sol1 (n):
    result = []
    for i in range(n):
        num = i%5 + 1
        result.append(num)
    return result

# 2번 : (2 + (1,3,4,5)) 반복
def sol2 (n):
    result=[]
    cnt=0
    while cnt < n:
        if cnt%2 == 0:
            result.append(2)
        else:
            arr = [1, 3, 4, 5]
            num = (cnt//2)%4
            result.append(arr[num])
        cnt += 1
    return result

# 3번 : (3,3, 1,1, 2,2, 4,4, 5,5) 반복
def sol3(n):
    result = []
    arr = [3, 1, 2, 4, 5]
    cnt = 0
    while cnt < n:
        num = (cnt//2) %5
        result.append(arr[num])
        cnt += 1
    return result

def correctCnt(a, answers):
    cnt = 0
    for i in range(len(answers)):
        if a[i] == answers[i]:
            cnt += 1
    return cnt

def solution (answers) :
    answer = []
    n = len(answers)
    a1 = correctCnt(sol1(n), answers)
    a2 = correctCnt(sol2(n), answers)
    a3 = correctCnt(sol3(n), answers)
    tA = [a1, a2, a3]
    for i in range(len(tA)):
        if tA[i] == max(tA):
            answer.append(i+1)
    return answer


#테스트코드
ans1 = [1,2,3,4,5]
if (solution(ans1) == [1]) :
    print("Pass")
else :
    print("Fail")

ans2 = [1,3, 2,4,2]
if (solution(ans2) == [1,2,3]) :
    print("Pass")
else :
    print("Fail")