# 수 정렬하기 3 ,  10989문제 
import sys 
n = int(sys.stdin.readline()) # 입력되는 수의 개수
x = [0] * 10001 # 범위가 10000개 까지니까 입력하는 값에 해당하는 인덱스에 넣기 위해서 10001개를 생성 해준다. 
max = 0 # 입력 받은 숫자 중에 가장 큰 값을 기록 
for i in range(n): 
    a = int(sys.stdin.readline())
    if max < a: # max보다 큰지 판단
        max = a # 크다면 최대값으로 기록 
    x[a]+=1 # 입력한 숫자에 해당하는 리스트에 +1 
for i in range(max+1): # max 값이 입력된 숫자중에 가장 큰 값이니까 100001 까지 for 문을 돌리지 않고 max 까지만 돌리기 
    if x[i] > 0: # 각각의 숫자가 몇반이 입력 되었는지 판단. 0보다 크다면 
        for k in range(x[i]): # 그 개수만큼 반복 
            print(i) # i를 출력 
            
""" max 값 기록 없이 해결 
import sys  
n = int(sys.stdin.readline()) # 입력되는 수의 개수
x = [0] * 10001 # 범위가 10000개 까지니까 입력하는 값에 해당하는 인덱스에 넣기 위해서 10001개를 생성 해준다. 
max = 0 # 입력 받은 숫자 중에 가장 큰 값을 기록 
for i in range(n): 
    x[int(sys.stdin.readline())]+=1 
for i in range(10001): # max 값이 입력된 숫자중에 가장 큰 값이니까 100001 까지 for 문을 돌리지 않고 max 까지만 돌리기 
    if x[i] > 0: # 각각의 숫자가 몇반이 입력 되었는지 판단. 0보다 크다면 
        for k in range(x[i]): # 그 개수만큼 반복 
            print(i) # i를 출력 
"""
