import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def BFS(i, j):
    queue = [(i, j, 1)]
    front, rear = -1, 0
    while front != rear:
        front += 1
        y, x, depth = queue[front]
        for k in range(4):
            yy = y + dy[k]
            xx = x + dx[k]
            if 0 <= yy < N and 0 <= xx < N:
                if info[yy][xx] < info[y][x]:
                    queue.append((yy, xx, depth + 1))
                    rear += 1

    return depth


for tc in range(1, T + 1):
    N, K = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]

    max_length = 0
    for deep in range(1, K + 1):
        for i in range(N):
            for j in range(N):
                max_val = max(sum(info, []))
                start_points = []
                for l in range(N):
                    for m in range(N):
                        if info[l][m] == max_val:
                            start_points.append((l, m))

                info[i][j] -= deep

                for start in start_points:
                    y, x = start
                    path_length = BFS(y, x)
                    if max_length < path_length:
                        max_length = path_length
                info[i][j] += deep

    print('#{} {}'.format(tc, max_length))
