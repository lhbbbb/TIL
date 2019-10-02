import sys

sys.stdin = open('input.txt', 'r')

T = int(input())


def backtrack(k, dist, path):
    global min_val
    if k == N:
        total_dist = abs(lst[1][0] - path[0]) + abs(lst[1][1] - path[1]) + dist
        if min_val > total_dist:
            min_val = total_dist
    else:
        for i in range(N):
            if visited[i]:
                continue
            if min_val > dist:
                diff = abs(paths[i][0] - path[0]) + abs(paths[i][1] - path[1])
                visited[i] = True
                backtrack(k + 1, dist + diff, paths[i])
                visited[i] = False


for tc in range(1, T + 1):
    N = int(input())

    lst = list(map(int, input().split()))

    lst = [(lst[i], lst[i + 1]) for i in range(0, (N + 2) * 2, 2)]

    paths = lst[2:]
    visited = [0] * N
    min_val = 1e8
    backtrack(0, 0, lst[0])

    print('#{} {}'.format(tc, min_val))
