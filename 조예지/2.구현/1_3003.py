# 원래 말 수 저장
default =[1, 1, 2, 2, 2, 8]
# 현재 가진 말 수 리스트에 저장하기
ps = list(map(int, input().split()))
# 비교하며 차이 한 줄로 출력하기
# 기본 print는 개행문자가 마지막에 들어가므로 뒤에 end=' '를 붙여주면 한 줄로 출력가능
for i in range(6):
    print(default[i]-ps[i], end=' ')