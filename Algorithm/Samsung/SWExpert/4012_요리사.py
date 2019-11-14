import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def comb_r(k, s):
    if k == R:
        cases.append([c[::], [x for x in gredients if x not in c]])
    else:
        for i in range(s, N - R + 1 + k):
            c[k] = gredients[i]
            comb_r(k + 1, i + 1)


def comb_r2(k, s):
    if k == R:
        case.append(c[::])
    else:
        for i in range(s, nums - R + 1 + k):
            c[k] = lst[i]
            comb_r2(k + 1, i + 1)


def cal(i, j):
    return info[i][j] + info[j][i]


for tc in range(1, T + 1):
    N = int(input())

    info = [list(map(int, input().split())) for _ in range(N)]

    gredients = [x for x in range(N)]
    cases = []
    R = N // 2
    c = [0] * R
    comb_r(0, 0)
    min_val = 1e9
    for i in range(len(cases) // 2):
        nums = N // 2
        R = 2
        c = [0] * R
        lst = cases[i][0]
        case = []
        comb_r2(0, 0)
        A_case = case
        lst = cases[i][1]
        case = []
        comb_r2(0, 0)
        B_case = case
        A_synergy, B_synergy = 0, 0
        for A in A_case:
            A_synergy += cal(A[0], A[1])
        for B in B_case:
            B_synergy += cal(B[0], B[1])

        diff = abs(A_synergy - B_synergy)
        if min_val > diff:
            min_val = diff

    print('#{} {}'.format(tc, min_val))
