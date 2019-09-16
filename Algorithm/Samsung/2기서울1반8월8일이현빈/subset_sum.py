import sys

sys.stdin = open('sample_input.txt', 'r')


def my_sum(lst):
    summation = 0
    for ele in lst:
        summation += ele

    return summation


T = int(input())
for idx in range(1, T + 1):
    N, K = map(int,input().split())

    A = [x for x in range(1, 13)]

    cnt = 0
    for i in range(1 << len(A)):
        subset = []
        for j in range(len(A)):
            if i & (1 << j):
                subset.append(A[j])
        if len(subset) == N and my_sum(subset) == K:
            cnt += 1

    print('#{} {}'.format(idx, cnt))
