N = int(input())

board = [[0] * N for _ in range(N)]

dy = [-1, -1, 1, 1]
dx = [-1, 1, -1, 1]


def DFS(i, j, k):
    stack = [(i, j)]
    while stack:
        y, x = stack.pop()
        y += dy[k]
        x += dx[k]
        if y >= 0 and y < N and x >= 0 and x < N:
            if board[y][x] == 1:
                return 0
            stack.append((y, x))
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
            board[k][i] = 1
            flag = 0
            for j in range(4):
                if not DFS(k, i, j):
                    flag = 1
                    break
            if flag:
                visited[i] = False
                board[k][i] = 0
                continue
            backtrack(k + 1)
            visited[i] = False
            board[k][i] = 0


visited = [0] * N
cnt = 0
backtrack(0)
print(cnt)
