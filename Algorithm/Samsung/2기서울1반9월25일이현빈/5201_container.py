import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    w = list(map(int, input().split()))
    t = list(map(int, input().split()))

    max_val = 0
    cnt = 0
    for ti in t:
        i = 0
        tmp = []
        while i < len(w):
            if w[i] <= ti:
                tmp.append(w[i])
            i += 1
        if tmp:
            container = max(tmp)
            max_val += container
            w.remove(container)
        else:
            cnt += 1

    if cnt == len(t):
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, max_val))
