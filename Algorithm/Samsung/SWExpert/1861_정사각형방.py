import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def BFS(i, j):
    visited[i][j] = True
    queue = [(i, j, 1)]
    front, rear = -1, 0
    cnt = 1
    while front != rear:
        front += 1
        y, x, cnt = queue[front]
        for k in range(4):
            next_y = y + dy[k]
            next_x = x + dx[k]
            if next_y >= 0 and next_y < N and next_x >= 0 and next_x < N:
                if A[next_y][next_x] - A[y][x] == 1:
                    visited[next_y][next_x] = True
                    queue.append((next_y, next_x, cnt + 1))
                    rear += 1
    return cnt


for tc in range(1, T + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    points = []
    for i in range(N):
        for j in range(N):
            points.append((i, j, A[i][j]))

    points.sort(key=lambda x: x[2])

    max_val = 0
    room = 1e8
    cnt_mat = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    for ele in points:
        if not visited[ele[0]][ele[1]]:
            nums = BFS(ele[0], ele[1])
            cnt_mat[ele[0]][ele[1]] = nums
            if max_val < nums:
                max_val = nums

    for i in range(N):
        for j in range(N):
            if cnt_mat[i][j] == max_val:
                if room > A[i][j]:
                    room = A[i][j]

    print('#{} {} {}'.format(tc, room, max_val))
