import sys
from queue import PriorityQueue

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def is_wall(y, x):
    if 0 <= y < N and 0 <= x < N:
        return False
    else:
        return True


def dijkstra():
    D = [[float('inf')] * N for _ in range(N)]
    p = [[None] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    queue = PriorityQueue()
    queue.put((0, 0, 0))
    D[0][0] = 0

    for _ in range(N):
        for _ in range(N):
            # min_y, min_x = -1, -1
            # min_val = float('inf')

            # for i in range(N):
            #     for j in range(N):
            #         if not visited[i][j] and D[i][j] < min_val:
            #             min_val = D[i][j]
            #             min_y, min_x = i, j

            # 모든 노드를 한번 씩은 방문해야 하기때문에 이 코드를 넣어줘야한다.
            while True:
                val, min_y, min_x = queue.get()
                if not visited[min_y][min_x]:
                    break

            visited[min_y][min_x] = 1
            for k in range(4):
                y, x = min_y + dy[k], min_x + dx[k]
                if is_wall(y, x):
                    continue
                if info[y][x] > info[min_y][min_x]:
                    cost = info[y][x] - info[min_y][min_x] + 1
                else:
                    cost = 1

                if not visited[y][x] and D[min_y][min_x] + cost < D[y][x]:
                    D[y][x] = D[min_y][min_x] + cost
                    p[y][x] = (min_y, min_x)
                    queue.put((D[y][x], y, x))

    return D[-1][-1]


for tc in range(1, T + 1):
    N = int(input())

    info = []
    for _ in range(N):
        info.append(list(map(int, input().split())))

    minimum = dijkstra()

    print('#{} {}'.format(tc, minimum))
