import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def BFS(start):
    deactivated = [*start]
    activated = []
    cell_status = []
    act_cnt = 0
    cnt = 0
    deact_cnt = len(deactivated)
    while cnt < K + 1:
        # 번식 작업
        if activated:
            activated.sort(key=lambda x: x[2])
            while activated:
                y, x, energy = activated.pop()
                cell_status.append(energy)
                for k in range(4):
                    yy, xx = y + dy[k], x + dx[k]
                    if not visited[yy][xx]:
                        visited[yy][xx] = 1
                        region[yy][xx] = region[y][x]
                        deactivated.append([yy, xx, region[y][x]])
                        deact_cnt += 1
        # 죽은 셀 빼내기
        i = 0
        while i < len(cell_status):
            cell_status[i] -= 1
            if cell_status[i] == 0:
                cell_status.pop(i)
                act_cnt -= 1
            else:
                i += 1
        # 활성 셀 찾기
        i = 0
        while i < len(deactivated):
            if deactivated[i][2] == 0:
                y, x, energy = deactivated.pop(i)
                activated.append((y, x, region[y][x]))
                act_cnt += 1
                deact_cnt -= 1
            else:
                deactivated[i][2] -= 1
                i += 1

        cnt += 1

    return act_cnt + deact_cnt


for tc in range(1, T + 1):
    N, M, K = map(int, input().split())

    region = [[0] * (2 * M + K) for _ in range(2 * N + K)]
    visited = [[0] * (2 * M + K) for _ in range(2 * N + K)]

    init_y = (2 * N + K) // 2
    init_x = (2 * M + K) // 2

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
    # 3. 살아있는 개수
    live_cnt = BFS(points)

    print('#{} {}'.format(tc, live_cnt))
