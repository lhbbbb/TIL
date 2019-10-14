N, L, R = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def BFS(i, j):
    queue = [(i, j)]
    visited[i][j] = True
    front, rear = -1, 0
    pop_total = board[i][j]
    while front != rear:
        front += 1
        y, x = queue[front]
        for k in range(4):
            next_y = y + dy[k]
            next_x = x + dx[k]
            if next_y >= 0 and next_y < N and next_x >= 0 and next_x < N:
                diff = abs(board[y][x] - board[next_y][next_x])
                if L <= diff <= R:
                    if not visited[next_y][next_x]:
                        visited[next_y][next_x] = True
                        pop_total += board[next_y][next_x]
                        queue.append((next_y, next_x))
                        rear += 1
    if rear == 0:
        return 0
    else:
        return (pop_total // (rear + 1)), queue


def DFS(i, j):
    stack = [(i, j)]
    visited[i][j] = True
    rear = 0
    pop_total = board[i][j]
    cnt = 0
    while rear != -1:
        y, x = stack[rear]
        rear -= 1
        for k in range(4):
            next_y = y + dy[k]
            next_x = x + dx[k]
            if next_y >= 0 and next_y < N and next_x >= 0 and next_x < N:
                diff = abs(board[y][x] - board[next_y][next_x])
                if L <= diff <= R:
                    if not visited[next_y][next_x]:
                        visited[next_y][next_x] = True
                        pop_total += board[next_y][next_x]
                        stack.append((next_y, next_x))
                        cnt += 1
                        rear = cnt
    if cnt == 0:
        return 0
    else:
        return (pop_total // (cnt + 1)), stack


mov_cnt = 0
while True:
    visited = [[0] * N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                info = BFS(i, j)
                if info:
                    for ele in info[1]:
                        board[ele[0]][ele[1]] = info[0]
                    flag = True
    if flag:
        mov_cnt += 1
    else:
        break

print(mov_cnt)
