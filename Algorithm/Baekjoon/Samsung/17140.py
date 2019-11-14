r, c, k = map(int, input().split())
r, c = r - 1, c - 1
A = [list(map(int, input().split())) for _ in range(3)]


def oper():
    max_len = 0
    for row in range(len(A)):
        tmp = [0] * 101
        for ele in A[row]:
            tmp[ele] += 1
        sorted_lst = []
        compare = 0
        for idx, value in enumerate(tmp):
            if idx != 0 and value != 0:
                if compare <= value:
                    compare = value
                    sorted_lst += [idx, value]
                else:
                    sorted_lst = [idx, value] + sorted_lst
        lst_len = len(sorted_lst)
        for i in range(0, lst_len - 2, 2):
            if sorted_lst[i + 1] == sorted_lst[i + 3]:
                if sorted_lst[i] > sorted_lst[i + 2]:
                    sorted_lst[i], sorted_lst[i + 2] = sorted_lst[i + 2], sorted_lst[i]

        if lst_len > 100:
            A[row] = sorted_lst[:100]
        else:
            A[row] = sorted_lst

        if max_len < lst_len:
            max_len = lst_len

    for row in range(len(A)):
        A[row] += [0] * (max_len - len(A[row]))


# 연산 정하기
cnt = 0
i = 0
while True:
    if i > 10:
        break
    i += 1
    r_len = len(A)
    c_len = len(A[0])
    if 0 <= r < r_len and 0 <= c < c_len:
        if A[r][c] == 100:
            print(-1)
            break
        elif A[r][c] == k:
            print(cnt)
            break
    if r_len >= c_len:
        cnt += 1
        oper()
    else:
        cnt += 1
        A = list(zip(*A))
        oper()
        A = list(zip(*A))
    for row in A:
        print(row)
    print()
