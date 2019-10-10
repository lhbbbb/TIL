N = int(input())

matrix = []

for _ in range(N):
    a, b = map(int, input().split())
    matrix.append(a)

matrix.append(b)

dp = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N - i):
        if i == 0:
            continue
        else:
            candi = []
            for k in range(j, j + i):
                candi.append(dp[j][k] + dp[k + 1][j + i] + matrix[j] * matrix[k + 1] * matrix[j + i + 1])
            dp[j][j + i] = min(candi)

print(dp[0][-1])

# 4
# 5 3
# 3 2
# 2 6
# 6 5
