N, M = map(int, input().split())

status = [list(map(int, input().split())) for _ in range(N)]


def comb_r(k, s):
    if k == M:
        return cases.append(c[::])
    else:
        for i in range(s, nums - M + 1 + k):
            c[k] = virus_loc[i]
            comb_r(k + 1, i + 1)


def BFS(lst):
    global tmp_cnt
    queue = []
    front, rear = -1, -1
    for ele in lst:
        i, j = ele
        visited[i][j] = True
        queue.append((i, j, 0))
        rear += 1

    while front != rear:
        front += 1
        y, x, depth = queue[front]
        for k in range(4):
            yy = y + dy[k]
            xx = x + dx[k]
            if 0 <= yy < N and 0 <= xx < N:
                if not visited[yy][xx] and tmp[yy][xx] != -1:
                    visited[yy][xx] = True
                    queue.append((yy, xx, depth + 1))
                    rear += 1
                    if tmp[yy][xx] == -3:
                        tmp[yy][xx] = depth + 1
                        tmp_cnt -= 1


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

virus_loc = []
zero_cnt = 0
for i in range(N):
    for j in range(N):
        if status[i][j] == 2:
            virus_loc.append((i, j))
            status[i][j] = 0
        elif status[i][j] == 0:
            zero_cnt += 1
            status[i][j] = -3
        else:
            status[i][j] = -1

nums = len(virus_loc)
cases = []
c = [0] * M
comb_r(0, 0)

min_val = 1e8
flag = False
if zero_cnt == 0:
    print(0)
else:
    for case in cases:
        tmp = [[x for x in y] for y in status]
        visited = [[0] * N for _ in range(N)]
        tmp_cnt = zero_cnt
        BFS(case)

        if tmp_cnt == 0:
            flag = True
        else:
            continue
        cost = max(sum(tmp, []))
        if min_val > cost:
            min_val = cost

    if flag:
        print(min_val)
    else:
        print(-1)
