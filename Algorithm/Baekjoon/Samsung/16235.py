from collections import deque

N, M, K = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
land = [[5] * N for _ in range(N)]

tree_loc = [[deque() for _ in range(N)] for _ in range(N)]

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(M):
    x, y, z = map(int, input().split())
    tree_loc[x - 1][y - 1].append(z)

for _ in range(K):
    # Spring
    dead = []
    birth = []
    for i in range(N):
        for j in range(N):
            if tree_loc[i][j]:
                k = 0
                length = len(tree_loc[i][j])
                while k < length:
                    if tree_loc[i][j][k] <= land[i][j]:
                        land[i][j] -= tree_loc[i][j][k]
                        tree_loc[i][j][k] += 1
                    else:
                        break
                    k += 1
                for _ in range(length - k):
                    dead.append((i, j, tree_loc[i][j].pop()))

                for tree in tree_loc[i][j]:
                    if tree % 5 == 0:
                        birth.append((i, j))
    # Summer
    for ele in dead:
        land[ele[0]][ele[1]] += ele[2] // 2

    # Fall
    for i, j in birth:
        for direction in range(8):
            next_y = i + dy[direction]
            next_x = j + dx[direction]
            if next_y >= 0 and next_y < N and next_x >= 0 and next_x < N:
                tree_loc[next_y][next_x].appendleft(1)

    # Winter
    for r in range(N):
        for c in range(N):
            land[r][c] += A[r][c]

live_cnt = 0
for i in range(N):
    for j in range(N):
        live_cnt += len(tree_loc[i][j])

print(live_cnt)
