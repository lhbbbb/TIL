import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def baby_run(lst):
    tmp = sorted(lst)
    cnt = 0
    for i in range(len(tmp) - 1):
        diff = tmp[i + 1] - tmp[i]
        if diff == 1:
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            return 1
    return 0


def triplet(lst):
    c = [0] * 10
    for ele in lst:
        c[ele] += 1

    for ele in c:
        if ele == 3:
            return 1
    return 0


for tc in range(1, T + 1):
    numbers = list(map(int, input().split()))

    player1, player2 = [], []
    for i in range(0, len(numbers), 2):
        player1.append(numbers[i])
        player2.append(numbers[i + 1])
        result_1 = baby_run(player1)
        result_2 = baby_run(player2)
        if result_1 > result_2:
            res_run = 1
        elif result_1 < result_2:
            res_run = 2
        else:
            res_run = 0

        result_1 = triplet(player1)
        result_2 = triplet(player2)
        if result_1 > result_2:
            res_tri = 1
        elif result_1 < result_2:
            res_tri = 2
        else:
            res_tri = 0

        if res_run != 0 and res_tri != 0:
            res = 0
        elif res_run > res_tri:
            res = res_run
        else:
            res = res_tri

        if res != 0:
            break
    print('#{} {}'.format(tc, res))
