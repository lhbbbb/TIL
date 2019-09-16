import sys

sys.stdin = open('sample_input.txt', 'r')


def rsp(p1, p2):
    if (lst[p1 - 1] == 1 and lst[p2 - 1] == 3) or (lst[p1 - 1] == 1 and lst[p2 - 1] == 1):
        return p1
    elif (lst[p1 - 1] == 2 and lst[p2 - 1] == 1) or (lst[p1 - 1] == 2 and lst[p2 - 1] == 2):
        return p1
    elif (lst[p1 - 1] == 3 and lst[p2 - 1] == 2) or (lst[p1 - 1] == 3 and lst[p2 - 1] == 3):
        return p1
    else:
        return p2


def backtrack(start, end):
    if start == end:
        return start
    else:
        p1 = backtrack(start, (start + end) // 2)
        p2 = backtrack((start + end) // 2 + 1, end)

    return rsp(p1, p2)


T = int(input())
for idx in range(1, T + 1):
    N = int(input())

    lst = list(map(int, input().split()))
    start = 1
    end = N
    winner = backtrack(start, N)

    print('#{} {}'.format(idx, winner))
