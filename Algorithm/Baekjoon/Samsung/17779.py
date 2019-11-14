N = int(input())

info = [list(map(int, input().split())) for _ in range(N)]


def check(d1, d2, y, x):
    if 0 <= y < y + d1 + d2 < N and 0 <= x - d1 < x < x + d2 < N:
        return 1
    else:
        return 0


def is_wall(y, x):
    if 0 <= y < N and 0 <= x < N:
        return 1
    else:
        return 0


def make_border(*args):
    d1, d2, i, j = args
    # 경계선 1
    dist = 0
    while dist <= d1:
        y = i + dist
        x = j - dist
        if is_wall(y, x):
            region[y][x] = 5
        else:
            break
        dist += 1
    # 경계선 2
    dist = 0
    while dist <= d2:
        y = i + dist
        x = j + dist
        if is_wall(y, x):
            region[y][x] = 5
        else:
            break
        dist += 1
    # 경계선 3
    dist = 0
    while dist <= d2:
        y = i + d1 + dist
        x = j - d1 + dist
        if is_wall(y, x):
            region[y][x] = 5
        else:
            break
        dist += 1
    # 경계선 4
    dist = 0
    while dist <= d1:
        y = i + d2 + dist
        x = j + d2 - dist
        if is_wall(y, x):
            region[y][x] = 5
        else:
            break
        dist += 1


def make_section(*args):
    d1, d2, i, j = args
    for l in range(i + d1):
        for m in range(j + 1):
            if region[l][m]:
                break
            region[l][m] = 1
    for l in range(i + d2 + 1):
        for m in range(N - 1, j, -1):
            if region[l][m]:
                break
            region[l][m] = 2
    for l in range(i + d1, N):
        for m in range(j - d1 + d2):
            if region[l][m]:
                break
            region[l][m] = 3
    for l in range(i + d2 + 1, N):
        for m in range(N - 1, j - d1 + d2 - 1, -1):
            if region[l][m]:
                break
            region[l][m] = 4


def find_diff():
    lst = [0] * 5
    for i in range(N):
        for j in range(N):
            if region[i][j] == 1:
                lst[0] += info[i][j]
            elif region[i][j] == 2:
                lst[1] += info[i][j]
            elif region[i][j] == 3:
                lst[2] += info[i][j]
            elif region[i][j] == 4:
                lst[3] += info[i][j]
            else:
                lst[4] += info[i][j]
    return max(lst) - min(lst)


min_val = 1e9
for i in range(N):
    for j in range(N):
        for d1 in range(1, N - 1):
            for d2 in range(1, N - 1):
                if not check(d1, d2, i, j):
                    continue
                region = [[0] * N for _ in range(N)]
                # 1. 경계선 만들기
                make_border(d1, d2, i, j)
                # 2. 선거구 만들기
                make_section(d1, d2, i, j)
                # 3. 케이스 최대-최소
                diff = find_diff()
                # 4. 최솟값 구하기
                if min_val > diff:
                    min_val = diff

print(min_val)