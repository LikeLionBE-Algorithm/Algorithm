cnt = 1
while True :
    result=0
    L, P, V = map(int, input().split())
    #0 0 0 나오면 종료
    if (L == P == V == 0) :
        break

    #P일 동안은 최대 L일 이용
    result += L * (V//P)

    #나머지 일수가 L보다 많으면 L일 만큼, 적으면 남은 기간 다 이용
    if (V%P > L) :
        result += L
    else:
        result += V%P
    print(f"Case {cnt}: {result}")
    cnt += 1
