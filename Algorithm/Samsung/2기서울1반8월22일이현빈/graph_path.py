import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def DFS(v):
    visited[v] = True
    for i in range(1, V + 1):
        if adj_matrix[v][i] and not visited[i]:
            DFS(i)


for idx in range(1, T + 1):
    V, E = map(int, input().split())

    adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        start, goal = map(int, input().split())
        adj_matrix[start][goal] = 1

    S, G = map(int, input().split())
    visited = [0] * (V + 1)
    DFS(S)
    if visited[G] == 1:
        print('#{} {}'.format(idx, 1))
    else:
        print('#{} {}'.format(idx, 0))