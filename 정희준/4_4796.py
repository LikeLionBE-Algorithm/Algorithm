import sys
x = [] # 최대 사용가능한 일수 저장 
while True:
    L,P,V = map(int,sys.stdin.readline().split())
    if L == 0 and P == 0 and V == 0 :
        break
    total = (V//P)*L
    if V-((V//P)*P) >= L:
        total+=L
    else:
        total+=(V-((V//P)*P))
    x.append(total)
for i in range(len(x)):
    print("Case",str(i+1)+":",x[i])