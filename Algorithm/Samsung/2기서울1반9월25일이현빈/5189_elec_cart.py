import sys

sys.stdin = open("sample_input.txt", 'r')

T = int(input())


def path(k, total, section):
    global min_val
    if k == N - 1:
        total += table[section][0]
        if min_val > total:
            min_val = total
    else:
        for i in range(1, N):
            if visited[i] or table[section][i] == 0:
                continue
            visited[i] = True
            new_total = total + table[section][i]
            if min_val > new_total:
                path(k + 1, new_total, i)
            visited[i] = False

for tc in range(1, T + 1):
    N = int(input())

    table = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    min_val = 1000000
    path(0, 0, 0)
    print('#{} {}'.format(tc, min_val))
