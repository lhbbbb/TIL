import sys

sys.stdin = open("input3.txt", 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    time_lst = [list(map(int, input().strip().split(' '))) for _ in range(N)]
    lst = [[0] * 150 for _ in range(N)]
    for idx, ele in enumerate(time_lst):
        lst[idx][ele[0]:ele[1]] = [1] * (ele[1] - ele[0])

    sum_lst = [sum(x) for x in zip(*lst)]
    print(max(sum_lst))
