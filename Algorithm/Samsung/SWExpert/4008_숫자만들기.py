import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def backtrack(k):
    global min_val, max_val
    if k == depth:
        tmp_nums = nums[::]

        for idx in range(1, N):
            tmp_nums[idx] = calcultate(tmp_nums[idx - 1], tmp_nums[idx], c[idx - 1])
        if min_val > tmp_nums[-1]:
            min_val = tmp_nums[-1]
        if max_val < tmp_nums[-1]:
            max_val = tmp_nums[-1]
    else:
        pruning = {}
        pruning[k] = {"+": 0, "-": 0, "*": 0, "/": 0}
        for i in range(depth):
            if visited[i]:
                continue
            c[k] = operators[i]
            if pruning[k][c[k]] != 0:
                continue
            else:
                pruning[k][c[k]] += 1

            visited[i] = True
            backtrack(k + 1)
            c[k] = 0
            visited[i] = False


def calcultate(x, y, op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    else:
        if x < 0:
            return -((-x) // y)
        else:
            return x // y


for tc in range(1, T + 1):
    N = int(input())

    # 수식에 사용되는 연산자
    a, b, c, d = map(int, input().split())
    operators = []
    for i in range(a):
        operators += ["+"]
    for i in range(b):
        operators += ["-"]
    for i in range(c):
        operators += ['*']
    for i in range(d):
        operators += ['/']
    depth = len(operators)
    # 수식에 사용되는 숫자
    nums = list(map(int, input().split()))
    visited = [0] * depth
    c = [0] * depth

    # 백트래킹
    min_val = 1e10
    max_val = -1e10
    backtrack(0)
    print('#{} {}'.format(tc, max_val - min_val))
