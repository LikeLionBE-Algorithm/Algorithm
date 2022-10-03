'''
BOJ_4796_캠핑

나의 idea : 휴가기간을 연속일수로 나눈만큼 round 갯수이므로, 여기에 실제 가능한 일수를 곱함.
나머지는 실제 가능한 일수가 크거나 나머지 휴가기간이 크거나로 나눠 계산
- 문자열 포맷팅 : "Case {0}: {1}".format(case, result)
'''

case = 0
while(True):
    L, P, V = map(int, input().split())
    if L==0 and P==0 and V==0:
        break
    result = (V//P)*L
    mod = V%P
    if mod >= L:
        result += L
    else:
        result += mod
    case += 1
    print("Case {0}: {1}".format(case, result))

