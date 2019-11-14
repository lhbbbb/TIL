import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def shape(num):
    if num == 1:
        return [(-1, 0), (1, 0), (0, 1), (0, -1)]
    elif num == 2:
        return [(-1, 0), (1, 0)]
    elif num == 3:
        return [(0, -1), (0, 1)]
    elif num == 4:
        return [(-1, 0), (0, 1)]
    elif num == 5:
        return [(1, 0), (0, 1)]
    elif num == 6:
        return [(1, 0), (0, -1)]
    else:
        return [(-1, 0), (0, -1)]


def is_connect(*args):
    yy, xx, arrow = args
    if (-arrow[0], -arrow[1]) in shape(info[yy][xx]):
        return True
    else:
        return False


def BFS(i, j):
    queue = [(i, j, 1)]
    front, rear = -1, 0
    visited[i][j] = 1
    cnt = 0
    while front != rear:
        front += 1
        y, x, depth = queue[front]
        d = shape(info[y][x])
        if depth == L:
            return rear + 1
        for k in range(len(d)):
            yy = y + d[k][0]
            xx = x + d[k][1]
            if 0 <= yy < N and 0 <= xx < M:
                if not visited[yy][xx] and info[yy][xx] != 0:
                    if is_connect(yy, xx, d[k]):
                        visited[yy][xx] = depth + 1
                        queue.append((yy, xx, depth + 1))
                        rear += 1
    return rear + 1


for tc in range(1, T + 1):
    # 세로, 가로, 세로 위치, 가로 위치, 탈출 소요시간
    N, M, R, C, L = map(int, input().split())

    info = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * M for _ in range(N)]
    loc_cnt = BFS(R, C)

    print('#{} {}'.format(tc, loc_cnt))
