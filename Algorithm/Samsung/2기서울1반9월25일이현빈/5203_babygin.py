import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def baby_run(lst):
    tmp = sorted(list(set(lst)))
    cnt = 0
    for i in range(len(tmp) - 1):
        diff = tmp[i + 1] - tmp[i]
        if diff == 1:
            cnt += 1
        else:
            cnt = 0
        if cnt >= 2:
            return 1
    return 0


def triplet(lst):
    c = [0] * 10
    for ele in lst:
        c[ele] += 1

    for ele in c:
        if ele >= 3:
            return 1
    return 0


for tc in range(1, T + 1):
    numbers = list(map(int, input().split()))

    player1, player2 = [], []
    result1, result2, res = 0, 0, 0
    for i in range(0, len(numbers), 2):
        player1.append(numbers[i])

        if baby_run(player1) or triplet(player1):
            result1 = 1
        else:
            result1 = 0
        if result1 > result2:
            res = 1
            break
        else:
            res = 0

        player2.append(numbers[i + 1])
        if baby_run(player2) or triplet(player2):
            result2 = 1
        else:
            result2 = 0
        if result2 > result1:
            res = 2
            break
        else:
            res = 0
        if res != 0 or result1 != 0 or result2 != 0:
            break
    print('#{} {}'.format(tc, res))
