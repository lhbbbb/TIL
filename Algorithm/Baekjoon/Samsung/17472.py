N, M = map(int, input().split())

info = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def BFS(i, j, num):
    global island
    queue = [(i, j)]
    visited[i][j] = True
    info[i][j] = num
    front, rear = -1, 0
    while front != rear:
        front += 1
        y, x = queue[front]
        for k in range(4):
            next_y = y + dy[k]
            next_x = x + dx[k]
            if (0 <= next_y < N) and (0 <= next_x < M):
                if not visited[next_y][next_x] and info[next_y][next_x] != 0:
                    info[next_y][next_x] = num
                    visited[next_y][next_x] = True
                    queue.append((next_y, next_x))
                    rear += 1
    island += queue


def find_cost(i, j, num):
    for k in range(4):
        y = i + dy[k]
        x = j + dx[k]
        if 0 <= y < N and 0 <= x < M:
            if info[y][x] == num:
                continue
            cnt = 0
            while info[y][x] == 0:
                cnt += 1
                y += dy[k]
                x += dx[k]


# 섬 번호 매기기
visited = [[0] * M for _ in range(N)]
num = 1
island = []
for i in range(N):
    for j in range(M):
        if info[i][j] and not visited[i][j]:
            BFS(i, j, num)
            num += 1

# 다리 코스트 구하기
adj_matrix = [[0] * (num + 1) for _ in range(num + 1)]
# 섬 연결관계 그래프 만들기

# 최소 비용 구하기
