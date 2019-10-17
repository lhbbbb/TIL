import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def makeset(x):
    p[x] = x


def findset(x):
    if x == p[x]:
        return x
    else:
        return findset(p[x])


def union(x, y):
    p[findset(y)] = findset(x)


for tc in range(1, T + 1):
    N, M = map(int, input().split())

    info = list(map(int, input().split()))

    p = [0] * (N + 1)
    for i in range(1, N + 1):
        makeset(i)

    for i in range(0, len(info), 2):
        union(info[i], info[i + 1])

    cnt = 0
    for i in range(1, N + 1):
        if i == p[i]:
            cnt += 1
    print("#{} {}".format(tc, cnt))
