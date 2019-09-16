#import sys

#sys.stdin = open('sample_input.txt', 'r')


def BFS(start, goal):
    visited[start] = True
    queue = [(start, 1)]
    while queue:
        node = queue.pop(0)
        for vertex in range(1, V + 1):
            if adj_matrix[node[0]][vertex] and not visited[vertex]:
                visited[vertex] = 1
                queue.append((vertex, node[1] + 1))
                if vertex == goal:
                    return node[1]
    return 0


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())

    adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        s, g = map(int, input().split())
        adj_matrix[s][g] = 1
        adj_matrix[g][s] = 1

    S, G = map(int, input().split())
    visited = [0] * (V + 1)

    print('#{} {}'.format(tc, BFS(S, G)))
