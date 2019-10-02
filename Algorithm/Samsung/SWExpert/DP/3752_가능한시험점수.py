import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    numbers = list(map(int, input().split()))

    visited = [0] * 10001

    cases = {0}
    for ele in numbers:
        lst = []
        for case in cases:
            if not visited[ele+case]:
                visited[ele+case] = True
                lst.append(ele + case)
        cases.update(lst)
    print('#{} {}'.format(tc, len(cases)))
