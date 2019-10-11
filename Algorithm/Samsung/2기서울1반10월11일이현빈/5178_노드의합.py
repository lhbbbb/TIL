import sys
import math

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())

    height = int(math.log2(N))
    if (N - (1 << height)) % 2 == 0:
        N = N + 1
    value = {i: 0 for i in range(1, N + 1)}
    for _ in range(M):
        p, c = map(int, input().split())
        value[p] = c

    tree = [i for i in range(N + 1)]
    print(tree)
    i = len(tree) - 2
    while i != 0:
        cur = i
        i -= 2
        value[cur // 2] = value[tree[cur]] + value[tree[cur + 1]]
    print(value)
    print("#{} {}".format(tc, value[L]))
