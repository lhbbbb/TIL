N, M, D = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]


def comb_r(k, s):
    if k == R:
        cases.append(c[::])
    else:
        for i in range(s, M - R + 1 + k):
            c[k] = archers[i]
            comb_r(k + 1, i + 1)


def detect(y, x):
    min_val = 1e8
    flag = False
    kill_y, kill_x = 0, 0
    for i in range(N - 1, -1, -1):
        for j in range(M):
            if copy[i][j]:
                dist = abs(y - i) + abs(x - j)
                if dist <= D:
                    if min_val > dist:
                        min_val = dist
                        kill_y, kill_x = i, j
                    elif min_val == dist:
                        if j < kill_x:
                            kill_y, kill_x = i, j
                    flag = True

    if flag:
        return kill_y, kill_x, 1
    else:
        return kill_y, kill_x, 0


def turn():
    for i in range(N - 2, -1, -1):
        for j in range(M):
            copy[i + 1][j] = copy[i][j]
            copy[i][j] = 0


def backtrack(cnt, kill, loc):
    global max_val
    if cnt == N * M or kill == enemy_cnt:
        if max_val < kill:
            max_val = kill
    else:
        tmp = set()
        for archer in loc:
            enemy_y, enemy_x, flag = detect(archer[0], archer[1])
            if flag:
                tmp.add((enemy_y, enemy_x))
        for ele in tmp:
            copy[ele[0]][ele[1]] = 0
        copy[-1] = [0] * M
        turn()
        backtrack(sum(copy, []).count(0), kill + len(tmp), loc)


# Archer location
archers = [(N, x) for x in range(M)]
R = 3
c = [0] * R
cases = []
comb_r(0, 0)
# count enemy
enemy_cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j]:
            enemy_cnt += 1

# solve
max_val = 0
for ele in cases:
    copy = [[x for x in y] for y in board]
    backtrack(0, 0, ele)

print(max_val)
