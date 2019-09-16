input()
T = 3
for idx in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(M)]

    section = [[0] * (N + 1) for _ in range(N + 1)]

    cnt = 0
    for ele in lst:
        for i in range(N + 1):
            for j in range(N + 1):
                if i >= ele[0] and i <= ele[2] and j >= ele[1] and j <= ele[3]:
                    if not section[i][j]:
                        cnt += 1
                    section[i][j] = 1

    print('#{} {}'.format(idx, cnt))
