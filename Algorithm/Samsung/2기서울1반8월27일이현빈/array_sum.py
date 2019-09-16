import sys

sys.stdin = open('sample_input.txt', 'r')


def backtrack(row, line, total):
    global min_val
    if row == N:
        line.pop()
        if total < min_val:
            min_val = total
        return min_val
    else:
        for idx, ele in enumerate(lst[row]):
            if idx not in line:
                if (total + ele) < min_val:
                    line.append(idx)
                    backtrack(row + 1, line, total + ele)
        if line:
            line.pop()
    return min_val


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    lst = [list(map(int, input().split())) for _ in range(N)]

    min_val = 10000
    num = []
    minimum = backtrack(0, num, 0)

    print('#{} {}'.format(tc, minimum))
