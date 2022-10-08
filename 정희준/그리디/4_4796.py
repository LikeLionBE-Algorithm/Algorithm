import sys
x = [] # 최대 사용 가능한 일수를 입력 순서대로 저장할 공간
while True:
    L,P,V = map(int,sys.stdin.readline().split())
    if L == 0 and P == 0 and V == 0 : # 모두 0 을 입력하면 while문 탈출 
        break
    total = (V//P)*L  # 휴가 중 무조건 가능한 연속일수 계산 
    if V-((V//P)*P) >= L: # 나머지 남은 일수로 사용 가능한 일 수 계산
        total+=L
    else:
        total+=(V-((V//P)*P))
    x.append(total) # 각각의 테스트 케이스의 최대 사용 가능한 일수 저장 
for i in range(len(x)):
    print("Case",str(i+1)+":",x[i])
