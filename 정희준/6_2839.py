sugar = int(input()) # 가지고 가야할 설탕의 양 
total = 0 # 봉지의 개수 
while True:
    if sugar % 5 == 0 : # 5로 나누어 지면 while 문 탈출 
        total += (sugar // 5)
        break
    sugar -=3 # 5로 나누어 지지 않는다면 -3 
    total+=1 # -3 하면서 봉지의 개수 증가 
    if sugar == 0: # 봉지의 개수가 5로 나누어 떨어지지 않아도 -3 하다가 0이 되면 탈출 
        break
    elif sugar < 0: # 봉지의 개수가 5로 나누어 떨어지지 않아도 -3 하다 0보다 작아지면 탈출 
        total = -1 # 설탕의 양을 5,3키로 봉지로 가지고 갈 수 없기 때문에 -1 저장 
        break
print(total) 










