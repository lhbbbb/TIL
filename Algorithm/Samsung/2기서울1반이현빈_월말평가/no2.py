import sys

sys.stdin = open('input2.txt', 'r')

T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def perm_r(k):
    if k == R:
        cases.append(c[::])
    else:
        for i in range(N):
            if visited[i]:
                continue
            visited[i] = True
            c[k] = snack[i]
            perm_r(k + 1)
            visited[i] = False


def BFS(point, target):
    queue = [(point[0], point[1], 0)]
    front, rear = -1, 0
    cnt = 0
    while front != rear:
        front += 1
        y, x, cnt = queue[front]
        for k in range(4):
            next_y = y + dy[k]
            next_x = x + dx[k]
            if next_y >= 0 and next_y < 10 and next_x >= 0 and next_x < 10:
                if lst[next_y][next_x] != target and not visited_bfs[next_y][next_x]:
                    visited_bfs[next_y][next_x] = 1
                    queue.append((next_y, next_x, cnt + 1))
                    rear += 1
                elif lst[next_y][next_x] == target:
                    cnt += 1
                    return cnt


for tc in range(1, T + 1):
    input()
    lst = [list(map(int, input().split())) for _ in range(10)]

    # 9 좌표 찾기
    points = []
    for i in range(10):
        for j in range(10):
            if lst[i][j] == 9:
                points.append((i, j))

    # 경우의 수 구하기
    cases = []
    snack = [1, 2, 3, 4, 5, 6]
    N = 6
    visited = [0] * 6
    R = 6
    c = [0] * 6
    perm_r(0)
    min_val = 1000000
    for case in cases:
        dist = 0
        flag = False
        for i in range(6):
            visited_bfs = [[0] * 10 for _ in range(10)]
            if min_val > dist:
                dist += BFS(points[i], case[i])
        if min_val > dist:
            min_val = dist

    print('#{} {}'.format(tc, min_val))
