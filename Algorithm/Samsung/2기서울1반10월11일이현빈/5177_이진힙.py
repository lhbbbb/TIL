import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    numbers = list(map(int, input().split()))

    tree = [0]
    for ele in numbers:
        if len(tree) == 1:
            tree.append(ele)
        else:
            tree.append(ele)
            i = len(tree) - 1
            while i != 1:
                cur = i
                i //= 2
                if tree[i] > tree[cur]:
                    tree[i], tree[cur] = tree[cur], tree[i]
    i = len(tree) - 1
    total = 0
    while i != 1:
        i //= 2
        total += tree[i]

    print("#{} {}".format(tc, total))
