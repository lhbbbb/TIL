import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def f(n):
    if n <= 1:
        return 1
    else:
        if 2*f(n-2) + f(n-1) not in memo:
            memo.append(2*f(n-2) + f(n-1))
        return memo[n]


for idx in range(1, T + 1):
    N = int(input())

    N = N // 10
    memo = [0, 1]
    print('#{} {}'.format(idx, f(N)))