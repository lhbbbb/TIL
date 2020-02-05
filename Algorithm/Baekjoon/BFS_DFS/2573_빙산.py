N, M = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
year = 0
iceberg_cnt = N * M - sum(info, []).count(0)


def BFS(i, j):
    queue = [(i, j)]
    visited[i][j] = True
    front, rear = -1, 0
    while front != rear:
        front += 1
        y, x = queue[front]
        for k in range(4):
            yy = y + dy[k]
            xx = x + dx[k]
            if info[yy][xx] and not visited[yy][xx]:
                visited[yy][xx] = 1
                queue.append((yy, xx))
                rear += 1


while True:
    # 1. 연결 관계 확인
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if info[i][j] and not visited[i][j]:
                BFS(i, j)
                cnt += 1

    # 2. 두 덩어리 이상이면 종료
    if cnt > 1:
        print(year)
        break

    # 3. 빙산 녹음
    tmp = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if info[i][j]:
                for k in range(4):
                    y = i + dy[k]
                    x = j + dx[k]
                    if info[y][x] == 0:
                        tmp[i][j] -= 1

    for i in range(N):
        for j in range(M):
            if info[i][j]:
                info[i][j] += tmp[i][j]
                if info[i][j] <= 0:
                    info[i][j] = 0
                    iceberg_cnt -= 1

    year += 1
    # 4. 빙산 다 녹음
    if iceberg_cnt == 0:
        print(0)
        break
