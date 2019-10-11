import sys

sys.stdin = open('input.txt', 'r')

T = 10


def cal(a, oper, b):
    if oper == "+":
        return a + b
    elif oper == "-":
        return a - b
    elif oper == "*":
        return a * b
    else:
        return a / b


for tc in range(1, T + 1):
    N = int(input())

    value = {}
    tree = {k: 0 for k in range(1, N + 1)}
    oper = "*/-+"
    for _ in range(N):
        lst = list(input().split())
        if lst[1] in oper:
            tree[int(lst[0])] = [int(lst[2]), int(lst[3])]
            value[int(lst[0])] = lst[1]
        else:
            value[int(lst[0])] = int(lst[1])
    # print(tree, value)
    i = N - 1
    while i != 0:
        cur = i
        i -= 2
        if tree[cur]:
            value[cur] = cal(value[tree[cur][0]], value[cur], value[tree[cur][1]])
        cur += 1
        if tree[cur]:
            value[cur] = cal(value[tree[cur][0]], value[cur], value[tree[cur][1]])
        if i == 0:
            cur = i + 1
            value[cur] = cal(value[tree[cur][0]], value[cur], value[tree[cur][1]])

    print("#{} {}".format(tc, int(value[1])))
