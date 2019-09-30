#import sys

#sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def backtrack(k, cost):
    global min_val
    if k == N:
        if min_val > cost:
            min_val = cost
    else:
        for i in range(N):
            if visited[i]:
                continue
            total_cost = cost + V[k][i]
            if min_val > total_cost:
                visited[i] = True
                backtrack(k + 1, total_cost)
                visited[i] = False


for tc in range(1, T + 1):
    N = int(input())

    V = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    min_val = 1000000
    backtrack(0, 0)
    print('#{} {}'.format(tc, min_val))