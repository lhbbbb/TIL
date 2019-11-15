import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def BFS(start):
    deactivated = [*start]
    activated = []
    cnt = 0
    deact_cnt = len(deactivated)
    tmp = []
    total = 0
    while cnt < K + 1:
        deactivated += tmp
        tmp = []
        if activated:
            # 번식 작업
            activated.sort(key=lambda x: x[2])
            while activated:
                y, x, energy = activated.pop()
                act_cnt[region[y][x]] += 1
                for k in range(4):
                    yy, xx = y + dy[k], x + dx[k]
                    if not visited[yy][xx]:
                        visited[yy][xx] = 1
                        region[yy][xx] = region[y][x]
                        tmp.append([yy, xx, region[y][x]])
                        deact_cnt += 1
        print(total + deact_cnt, total, deact_cnt, cnt)
        # for row in region:
        #     print(row)
        # print()
        # 활성 셀 찾기
        i = 0
        while i < len(deactivated):
            energy = deactivated[i][2]
            deactivated[i][2] -= 1
            if energy == 0:
                y, x, energy = deactivated.pop(i)
                energy = region[y][x]
                activated.append((y, x, energy))
                deact_cnt -= 1
            else:
                i += 1

        cnt += 1
        total = 0
        for i in range(1, 11):
            total += act_cnt[i]
            act_cnt[i - 1] = act_cnt[i]

    return deact_cnt


for tc in range(1, 2):
    N, M, K = map(int, input().split())

    region = [[0] * (M + K * 2) for _ in range(N + K * 2)]
    visited = [[0] * (M + K * 2) for _ in range(N + K * 2)]

    init_y = (N + K * 2) // 2
    init_x = (M + K * 2) // 2

    # 1. 세포 위치시키기
    points = []
    for i in range(N):
        info = list(map(int, input().split()))
        for j in range(M):
            y = init_y + i
            x = init_x + j
            if info[j] != 0:
                region[y][x] = info[j]
                visited[y][x] = 1
                points.append([y, x, info[j]])

    # 2. 세포 활성화 & 번식
    act_cnt = {}
    for i in range(11):
        act_cnt[i] = 0

    # 3. 살아있는 개수
    live_cnt = BFS(points)

    for i in range(1, 11):
        live_cnt += act_cnt[i]

    print('#{} {}'.format(tc, live_cnt))
