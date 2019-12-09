def solution(m, n, puddles):
    board = [[0] * m for _ in range(n)]
    dy = [-1, 0]
    dx = [0, -1]
    board[0][0] = 1
    for puddle in puddles:
        x, y = puddle
        board[y - 1][x - 1] = -1
    for i in range(n):
        for j in range(m):
            if board[i][j] == -1:
                continue
            for k in range(2):
                yy = i + dy[k]
                xx = j + dx[k]
                if 0 <= yy < n and 0 <= xx < m:
                    if board[yy][xx] == -1:
                        continue
                    board[i][j] += board[yy][xx]

    answer = board[-1][-1] % 1000000007
    return answer