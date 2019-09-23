import sys

sys.stdin = open("input3.txt", 'r')

T = int(input())

# def search(k):
#     if k == N:
#         print(c)
#     else:
#         if time_lst[k][1] > time_lst[k + 1][0]:
#             c[k] = 1
#             search(k + 1)
#         c[k] = 0
#         search(k + 2)


for tc in range(1, T + 1):
    # N = int(input())
    #
    # time_lst = [list(map(int, input().strip().split(' '))) for _ in range(N)]
    # time_lst = sorted(time_lst)
    # c = [0] * N
    # search(0)
    # print(sorted(time_lst))
    N = int(input())
    time_lst = [list(map(int, input().strip().split(' '))) for _ in range(N)]
    lst = [[0] * 150 for _ in range(N)]
    for idx, ele in enumerate(time_lst):
        lst[idx][ele[0]:ele[1]] = [1] * (ele[1] - ele[0])

    sum_lst = [sum(x) for x in zip(*lst)]
    print(max(sum_lst))
