# todo: BFS를 호출하지 말고 미리 각 바이러스에 해당하는 테이블을 만든 다음에 그것을 참조하는 방법을 사용하자!!
def comb_r(k, s):
    if k == M:
        return cases.append(c[::])
    else:
        for i in range(s, nums - M + 1 + k):
            c[k] = virus_loc[i]
            comb_r(k + 1, i + 1)


def BFS(i, j):
    global tmp_cnt
    visited[i][j] = True
    queue = [(i, j, 0)]
    front, rear = -1, 0
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
                        virus_points.add((yy, xx))
                        tmp[yy][xx] = depth + 1


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, M = map(int, input().split())

status = [list(map(int, input().split())) for _ in range(N)]
virus_loc = []
zero_cnt = 0
# 바이러스 위치 찾기
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

# 바이러스 위치마다 전염 테이블 생성
virus_table = {}
virus_points = set()
for virus in virus_loc:
    tmp = [[x for x in y] for y in status]
    y, x = virus
    visited = [[0] * N for _ in range(N)]
    BFS(y, x)
    virus_table[virus] = tmp

for k, v in virus_table.items():
    for i in range(len(v)):
        print(v[i])
    print()

# 가능한 활성 바이러스 조합 만들기
nums = len(virus_loc)
cases = []
c = [0] * M
comb_r(0, 0)

min_val = 1e8
flag = False

# 검사
if zero_cnt == 0:
    print(0)
else:
    for case in cases:
        new_table = [[-1] * N for _ in range(N)]
        print(len(virus_points), zero_cnt)
        for ele in case:
            for point in virus_points:
                i, j = point
                if virus_table[ele][i][j] != -1 and virus_table[ele][i][j] > 0:
                    if new_table[i][j] == -1:
                        new_table[i][j] = virus_table[ele][i][j]
                    else:
                        if new_table[i][j] > virus_table[ele][i][j]:
                            new_table[i][j] = virus_table[ele][i][j]

        # if exists:
        #     flag = True
        # else:
        #     continue
        cost = max(sum(new_table, []))
        if min_val > cost:
            min_val = cost

    if flag:
        print(min_val)
    else:
        print(-1)
