def findset(x, p):
    if x == p[x]:
        return x
    else:
        return findset(p[x], p)


def union(y, x, p):
    p[findset(x, p)] = findset(y, p)
    return p


def solution(n, computers):
    visited = [[0] * n for _ in range(n)]
    answer = 0
    network = []
    for i in range(n):
        for j in range(n):
            if i == j or computers[i][j] == 0:
                continue
            if computers[i][j]:
                if visited[i][j]:
                    continue
                visited[i][j], visited[j][i] = 1, 1
                network.append((i, j))

    p = [x for x in range(n)]
    for y, x in network:
        if findset(y, p) == findset(x, p):
            continue
        p = union(y, x, p)

    for i, ele in enumerate(p):
        if i == ele:
            answer += 1

    return answer