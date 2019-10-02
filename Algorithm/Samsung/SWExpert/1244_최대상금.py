import sys

sys.stdin = open('input.txt', 'r')

T = int(input())


def backtrack(k):
    global max_val
    if not visited.get(k):
        visited[k] = []

    if info in visited[k]:
        return
    visited[k].append(info[::])

    if k == chance:
        val = int(''.join(info))
        if max_val < val:
            max_val = val
    else:
        for i in range(len(info) - 1):
            for j in range(i + 1, len(info)):
                info[i], info[j] = info[j], info[i]
                backtrack(k + 1)
                info[i], info[j] = info[j], info[i]


for tc in range(1, T + 1):
    info, chance = input().split()
    info = list(info)
    chance = int(chance)
    max_val = 0
    visited = {}
    backtrack(0)

    print('#{} {}'.format(tc, max_val))
