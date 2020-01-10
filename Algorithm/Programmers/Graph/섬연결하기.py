def findset(x, p):
    if x == p[x]:
        return x
    else:
        return findset(p[x], p)


def union(y, x, p):
    p[findset(x, p)] = findset(y, p)
    return p


def solution(n, costs):
    answer = 0
    costs = sorted(costs, key=lambda x: x[2])
    p = [x for x in range(n)]
    for start, end, cost in costs:
        if findset(start, p) != findset(end, p):
            p = union(end, start, p)
            answer += cost

    return answer