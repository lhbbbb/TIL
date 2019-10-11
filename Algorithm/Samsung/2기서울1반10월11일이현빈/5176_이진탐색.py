import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def traversal(node):
    global cnt
    if node == 0:
        return
    else:
        traversal(tree[0][node])
        if not visited[node]:
            visited[node] = True
            cnt += 1
            value[node] = cnt
        traversal(tree[1][node])


for tc in range(1, T + 1):
    N = int(input())

    for i in range(1, N):
        if 1 << i > N:
            num = i
            break

    tree = [[0] * (1 << num) for _ in range(2)]
    stack = [1]
    while stack:
        node = stack.pop()
        if 2 ** num >= node:
            for i in range(2):
                if node * 2 + i <= N:
                    tree[i][node] = node * 2 + i
                    stack.append(tree[i][node])
    visited = [0] * (1 << num)
    cnt = 0
    value = {}
    traversal(1)

    print('#{} {} {}'.format(tc, value[1], value[N // 2]))
