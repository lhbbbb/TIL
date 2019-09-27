import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

dy = [-1, 1, 0, 0, 1, 1, -1, -1]
dx = [0, 0, -1, 1, 1, -1, 1, -1]


def DFS(i, j, k, v_dfs):
    v_dfs[i][j] = 1
    stack = [(i, j)]
    while stack:
        y, x = stack.pop()
        next_y = y + dy[k]
        next_x = x + dx[k]
        if next_y >= 0 and next_y < N and next_x >= 0 and next_x < N:
            if not v_dfs[next_y][next_x]:
                stack.append((next_y, next_x))
            else:
                return 0
    return 1


def backtrack(k):
    global cnt
    if k == N:
        cnt += 1
    else:
        for i in range(N):
            if visited[i]:
                continue
            visited[i] = True
            lst[k][i] = 1
            flag = False
            for direction in range(8):
                if not DFS(k, i, direction, lst):
                    flag = True
                    break
            if flag:
                visited[i] = False
                lst[k][i] = 0
                continue
            else:
                backtrack(k + 1)
                visited[i] = False
                lst[k][i] = 0


for tc in range(1, T + 1):
    N = int(input())

    lst = [[0] * N for _ in range(N)]
    visited = [0] * N
    cnt = 0
    backtrack(0)

    print('#{} {}'.format(tc, cnt))
