import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())

    info = list(map(int, input().split()))
    tree = [[0] * (E + 2) for _ in range(2)]

    for i in range(0, len(info), 2):
        if tree[0][info[i]]:
            tree[1][info[i]] = info[i + 1]
        else:
            tree[0][info[i]] = info[i + 1]

    stack = [N]
    cnt = 0
    while stack:
        node = stack.pop()
        cnt += 1
        for i in range(2):
            if tree[i][node]:
                stack.append(tree[i][node])

    print("#{} {}".format(tc, cnt))
