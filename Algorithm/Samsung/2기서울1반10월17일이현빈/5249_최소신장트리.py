import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def findset(x):
    if x == p[x]:
        return x
    else:
        return findset(p[x])


def unionset(x, y):
    p[findset(y)] = findset(x)


for tc in range(1, T + 1):
    V, E = map(int, input().split())

    info = []
    for _ in range(E):
        info.append(list(map(int, input().split())))

    # sort edges by cost
    info.sort(key=lambda x: x[2])

    # find mst cost
    p = [x for x in range(V + 1)]
    cost = 0
    for ele in info:
        if findset(ele[0]) != findset(ele[1]):
            unionset(ele[0], ele[1])
            # print(p)
            cost += ele[2]

    print("#{} {}".format(tc, cost))
