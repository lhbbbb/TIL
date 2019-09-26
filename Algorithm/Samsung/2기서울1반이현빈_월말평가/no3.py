import sys
import time

sys.stdin = open('input3.txt', 'r')

T = int(input())


def backtrack(k, cost, total):
    global max_val
    if k == len(dist):
        return
    else:
        new_cost = cost + dist[k][0]
        if new_cost <= C:
            new_total = total + dist[k][1]
            if max_val < new_total:
                max_val = new_total
            backtrack(k + 1, new_cost, new_total)
        backtrack(k + 1, cost, total)


for tc in range(1, T + 1):
    s = time.time()
    N, M, C = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    # 미네랄 좌표 찾기
    points = []
    start = 0
    for i in range(N):
        for j in range(M):
            if lst[i][j] != 0 and lst[i][j] > 1:
                points.append((i, j, lst[i][j]))
            if lst[i][j] == 1:
                start = (i, j)
    dist = []
    for ele in points:
        energy = 2 * (abs(ele[0] - start[0]) + abs(ele[1] - start[1]))
        dist.append((energy, ele[2]))

    max_val = 0
    backtrack(0, 0, 0)

    print('#{} {}'.format(tc, max_val))
    end = time.time()
    print(end - s)
