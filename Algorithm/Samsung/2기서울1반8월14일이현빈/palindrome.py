import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for idx in range(1, T + 1):
    N, M = map(int, input().split())

    lst = [input() for i in range(N)]

    # row
    flag = False
    for ele in lst:
        for i in range(M):
            if (i + M) > N:
                break
            else:
                if ele[i:i + M] == ele[i:i + M][::-1]:
                    print('#{} {}'.format(idx, ele[i:i + M]))
                    flag = True
                    break
        if flag:
            break
    # col
    lst = [list(x) for x in zip(*lst)]
    for ele in lst:
        for i in range(M):
            if (i + M) > N:
                break
            else:
                if ele[i:i + M] == ele[i:i + M][::-1]:
                    print('#{} {}'.format(idx, ''.join(ele[i:i + M])))
                    flag = True
                    break
        if flag:
            break
