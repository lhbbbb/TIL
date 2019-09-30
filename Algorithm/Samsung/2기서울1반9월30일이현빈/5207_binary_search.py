import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def binary_search(l, r, lst, target, flag):
    mid = (l + r) // 2
    if lst[mid] < target:
        if flag == 'r':
            return 0
        if binary_search(mid + 1, r, lst, target, 'r'):
            return 1
        else:
            return 0
    elif lst[mid] > target:
        if flag == 'l':
            return 0
        if binary_search(l, mid - 1, lst, target, 'l'):
            return 1
        else:
            return 0
    else:
        return 1


for tc in range(1, T + 1):
    N, M = map(int, input().split())

    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    cnt = 0
    for ele in B:
        if ele in A:
            cnt += binary_search(0, len(A) - 1, A, ele, 0)

    print('#{} {}'.format(tc, cnt))
