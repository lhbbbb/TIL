import sys

sys.stdin = open("sample_input.txt", 'r')

T = int(input())

dy = (-1, 0)
dx = (0, -1)

for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 간선 세기
            edge_cnt = 0
            for k in range(2):
                y = i + dy[k]
                x = j + dx[k]
                if y >= 0 and x >= 0:
                    edge_cnt += 1
            # 최소값 구하기
            if edge_cnt == 0:
                pass
            elif edge_cnt == 1:
                for k in range(2):
                    y = i + dy[k]
                    x = j + dx[k]
                    if y >= 0 and x >= 0:
                        lst[i][j] += lst[y][x]
            else:
                min_val = 1000000
                for k in range(2):
                    y = i + dy[k]
                    x = j + dx[k]
                    if y >= 0 and x >= 0:
                        if min_val > lst[y][x]:
                            min_val = lst[y][x]
                lst[i][j] += min_val
    print('#{} {}'.format(tc, lst[N - 1][N - 1]))
