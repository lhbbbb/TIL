"""
1. list로 tree 구현
1번 메모리 낭비 심할 시 2. dic으로 tree 구현
그래도 문제 안 풀리면 3. class로 tree 구현
"""

import sys
import math

sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def in_order_traversal(node):
    if tree[node] == 0:
        return
    else:
        in_order_traversal(node * 2)
        numbers.append(node)
        in_order_traversal(node * 2 + 1)


for tc in range(1, T + 1):
    N = int(input())
    height = int(math.log2(N)) + 2
    tree = [i for i in range(N + 1)]
    tree += [0] * ((1 << height) - N + 1)
    numbers = []
    in_order_traversal(1)
    print(tree, numbers)
    for i, ele in enumerate(numbers):
        if N // 2 == ele:
            index = i + 1
        elif ele == 1:
            root = i + 1
    print("#{} {} {}".format(tc, tree[root], tree[index]))
