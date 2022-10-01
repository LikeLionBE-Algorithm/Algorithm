time = int(input())  # 총 요리시간 입력 
option = [300,60,10] # 전자레인지 시간 옵션 
if (((time%300)%60)%10) > 0:
    print(-1)
else:
    for i in option:
     count = 0 
     count += time//i
     print(count,end = " ") # 각각의 옵션으로 나눈 값 줄 바꿈 없이 출력 
     time = time%i
