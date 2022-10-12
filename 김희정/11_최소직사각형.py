'''
Programmers : level1 최소직사각형
나의 idea :
1. w,h 중 가장 작은 값 pick
2. 배열 전체 돌면서 탐색
둘 중 큰수가 w,h중 큰 수 보다 작고, 둘 중 min은 result_min보다 작으면 통과
아니면 안되는걸로 update
'''

def solution(sizes):
    answer = 0
    w = []
    h = []
    for elem in sizes:
        w.append(elem[0])
        h.append(elem[1])
    result_w = min(w)
    result_h = min(h)

    result_max = max(result_h, result_w)
    result_min = min(result_h, result_w)

    for elem in sizes:
        bigger = max(elem)
        smaller = min(elem)
        if smaller >= result_min:
            result_min = smaller
        if bigger >= result_max:
            result_max = bigger

    answer = result_max*result_min
    return answer

if __name__ == '__main__':
    sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
    print(solution(sizes))

'''
[other solution]
- idea : 큰값 중 최댓값 * 작은값 중 최댓값
w,h 둘 중 큰거 모은 list, 작은거 모은 list >>  큰거 llst에서 최댓값과 작은거 list에서 최댓값의 조합
'''
def other_solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)