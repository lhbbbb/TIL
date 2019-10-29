import sys
from queue import PriorityQueue

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def dijkstra(i, j):
    global cnt
    queue = PriorityQueue()
    queue.put((0, i, j))
    # visited[i][j] = True
    while cnt:
        cost, y, x = queue.get()
        cnt -= 1
        while visited[y][x] == True and cnt:
            cost, y, x = queue.get()
        for k in range(4):
            next_y = y + dy[k]
            next_x = x + dx[k]
            if next_y >= 0 and next_y < N and next_x >= 0 and next_x < N:
                if not visited[next_y][next_x]:
                    if info[next_y][next_x] > info[y][x]:
                        dist_info[next_y][next_x] = min(dist_info[next_y][next_x],
                                                        dist_info[y][x] + (info[next_y][next_x] - info[y][x]) + 1)
                    else:
                        dist_info[next_y][next_x] = min(dist_info[next_y][next_x],
                                                        dist_info[y][x] + 1)

                    queue.put((dist_info[next_y][next_x], next_y, next_x))
        visited[y][x] = True


for tc in range(1, T + 1):
    N = int(input())
    cnt = N ** 2

    info = [list(map(int, input().split())) for _ in range(N)]

    dist_info = [[1e9] * N for _ in range(N)]
    dist_info[0][0] = 0
    visited = [[0] * N for _ in range(N)]
    dijkstra(0, 0)

    print('#{} {}'.format(tc, dist_info[-1][-1]))
