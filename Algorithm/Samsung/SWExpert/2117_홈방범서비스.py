import sys

sys.stdin = open("sample_input.txt", 'r')

T = int(input())


def check_house(i, j):
    cnt = 0
    # 중앙
    cent_y = i
    cent_x = j

    for row in range(k):
        y = cent_y + row
        if 0 <= y < N:
            cnt += check_house_col(y, cent_x, row)
        if row == 0:
            continue
        y = cent_y - row
        if 0 <= y < N:
            cnt += check_house_col(y, cent_x, row)
    return cnt


def check_house_col(i, j, data):
    cnt = 0
    for col in range(k - data):
        x = j - col
        if 0 <= x < N:
            if info[i][x]:
                cnt += 1
        if col == 0:
            continue
        x = j + col
        if 0 <= x < N:
            if info[i][x]:
                cnt += 1
    return cnt


for tc in range(1, T + 1):
    N, M = map(int, input().split())

    info = [list(map(int, input().split())) for _ in range(N)]

    # Maximum K 정하기
    house_cnt = 0
    for i in range(N):
        for j in range(N):
            if info[i][j]:
                house_cnt += 1
    for i in range(1, 150):
        revenue = M * house_cnt - (i ** 2 + (i - 1) ** 2)
        if revenue < 0:
            K = i - 1
            break

    # 각 도시 한 구역마다 돌면서 비용 확인
    ## 현재까지 구한 집 개수보다 구역에 들어간 집의 개수가 작으면 return
    max_val = 0
    for k in range(1, K + 1):
        cost = k ** 2 + (k - 1) ** 2
        for i in range(N):
            for j in range(N):
                region_cnt = check_house(i, j)
                if region_cnt < max_val:
                    continue
                revenue = M * region_cnt - cost
                if revenue < 0:
                    continue
                else:
                    if max_val < region_cnt:
                        max_val = region_cnt

    print('#{} {}'.format(tc, max_val))
