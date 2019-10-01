N, M = map(int, input().split())

info = [list(map(int, input().split())) for _ in range(N)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def backtrack(k, cnt, visit):
    global min_val
    if k == len(location):
        if min_val > cnt:
            min_val = cnt
    else:
        if info[location[k][0]][location[k][1]] == 1:
            for i in range(4):
                y, x = location[k][0], location[k][1]
                tmp_cnt = cnt
                new_visit = [[x for x in y] for y in visit]
                while True:
                    y += dy[i]
                    x += dx[i]
                    if y >= 0 and y < N and x >= 0 and x < M:
                        if info[y][x] == 6:
                            break
                        if info[y][x] == 0 and not new_visit[y][x]:
                            new_visit[y][x] = 1
                            tmp_cnt -= 1
                    else:
                        break
                backtrack(k + 1, tmp_cnt, new_visit)
        elif info[location[k][0]][location[k][1]] == 2:
            for i in range(2):
                tmp_cnt = cnt
                new_visit = [[x for x in y] for y in visit]
                for j in range(0, 3, 2):
                    y, x = location[k][0], location[k][1]
                    while True:
                        y += dy[i + j]
                        x += dx[i + j]
                        if y >= 0 and y < N and x >= 0 and x < M:
                            if info[y][x] == 6:
                                break
                            if info[y][x] == 0 and not new_visit[y][x]:
                                new_visit[y][x] = 1
                                tmp_cnt -= 1
                        else:
                            break
                backtrack(k + 1, tmp_cnt, new_visit)
        elif info[location[k][0]][location[k][1]] == 3:
            for i in range(3, 7):
                tmp_cnt = cnt
                new_visit = [[x for x in y] for y in visit]
                for j in range(2):
                    y, x = location[k][0], location[k][1]
                    while True:
                        y += dy[(i + j) % 4]
                        x += dx[(i + j) % 4]
                        if y >= 0 and y < N and x >= 0 and x < M:
                            if info[y][x] == 6:
                                break
                            if info[y][x] == 0 and not new_visit[y][x]:
                                new_visit[y][x] = 1
                                tmp_cnt -= 1
                        else:
                            break
                backtrack(k + 1, tmp_cnt, new_visit)
        elif info[location[k][0]][location[k][1]] == 4:
            for i in range(2, 6):
                tmp_cnt = cnt
                new_visit = [[x for x in y] for y in visit]
                for j in range(3):
                    y, x = location[k][0], location[k][1]
                    while True:
                        y += dy[(i + j) % 4]
                        x += dx[(i + j) % 4]
                        if y >= 0 and y < N and x >= 0 and x < M:
                            if info[y][x] == 6:
                                break
                            if info[y][x] == 0 and not new_visit[y][x]:
                                new_visit[y][x] = 1
                                tmp_cnt -= 1
                        else:
                            break
                backtrack(k + 1, tmp_cnt, new_visit)
        else:
            tmp_cnt = cnt
            new_visit = [[x for x in y] for y in visit]
            for i in range(4):
                y, x = location[k][0], location[k][1]
                while True:
                    y += dy[i]
                    x += dx[i]
                    if y >= 0 and y < N and x >= 0 and x < M:
                        if info[y][x] == 6:
                            break
                        if info[y][x] == 0 and not new_visit[y][x]:
                            new_visit[y][x] = 1
                            tmp_cnt -= 1
                    else:
                        break
            backtrack(k + 1, tmp_cnt, new_visit)


zero_cnt = 0
for i in range(N):
    zero_cnt += info[i].count(0)

location = []
for i in range(N):
    for j in range(M):
        if info[i][j] != 0 and info[i][j] != 6:
            location.append((i, j))

min_val = 1e8
visited = [[0] * M for _ in range(N)]
backtrack(0, zero_cnt, visited)
print(min_val)