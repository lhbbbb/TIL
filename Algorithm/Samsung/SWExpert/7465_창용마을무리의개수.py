import sys

sys.stdin = open('s_input.txt', 'r')

T = int(input())


def BFS(start):
    visited[start] = True
    queue = [start]
    front, rear = -1, 0
    while front != rear:
        front += 1
        node = queue[front]
        if graph.get(node):
            for next_node in graph[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)
                    rear += 1


for tc in range(1, T + 1):
    N, M = map(int, input().split())

    graph = {}
    # directed graph
    for _ in range(M):
        start, end = map(int, input().split())
        if not graph.get(start):
            graph[start] = set()
        if not graph.get(end):
            graph[end] = set()

        graph[start].add(end)
        graph[end].add(start)

    visited = [0] * (N + 1)
    cnt = 0
    for i in range(1, N + 1):
        if not visited[i]:
            BFS(i)
            cnt += 1

    print('#{} {}'.format(tc, cnt))
