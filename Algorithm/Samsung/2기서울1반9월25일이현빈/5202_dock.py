import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    work = [list(map(int, input().split())) for _ in range(N)]

    work = sorted(work)

    tmp = []
    candi = work[::]
    cnt = 0
    while candi:
        new_candi = set()
        for i in range(len(candi) - 1):
            for j in range(i + 1, len(candi)):
                if candi[i][1] <= candi[j][0]:
                    new_candi.add(tuple(candi[j]))
        candi = sorted(list(new_candi))
        cnt += 1

    print('#{} {}'.format(tc, cnt))
