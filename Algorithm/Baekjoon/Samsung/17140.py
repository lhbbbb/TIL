r, c, k = map(int, input().split())
r, c = r - 1, c - 1
A = [list(map(int, input().split())) for _ in range(3)]


def oper():
    max_len = 0
    for row in range(len(A)):
        tmp = [0] * 101
        max_val = 0
        for ele in A[row]:
            tmp[ele] += 1
            if max_val < tmp[ele]:
                max_val = tmp[ele]

        sorted_lst = []
        for i in range(1, max_val + 1):
            for idx, val in enumerate(tmp):
                if val == i and idx != 0:
                    sorted_lst += [idx, val]

        lst_len = len(sorted_lst)

        if lst_len > 100:
            A[row] = sorted_lst[:100]
        else:
            A[row] = sorted_lst

        if max_len < lst_len:
            max_len = lst_len

    for row in range(len(A)):
        A[row] += [0] * (max_len - len(A[row]))

    return max_len


# 연산 정하기
cnt = 0
r_len, c_len = len(A), len(A[0])
while True:
    if cnt > 100:
        print(-1)
        break
    if 0 <= r < r_len and 0 <= c < c_len:
        if A[r][c] == k:
            print(cnt)
            break
    cnt += 1
    if r_len >= c_len:
        c_len = oper()
    else:
        A = list(zip(*A))
        r_len = oper()
        A = list(zip(*A))
