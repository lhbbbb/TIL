import sys
from queue import PriorityQueue

sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def dijkstra(node):
    queue = PriorityQueue()
    queue.put((0, node))
    flag = False
    while True:
        cost, node = queue.get()
        while visited[node]:
            cost, node = queue.get()
        if graph.get(node):
            for next_node in graph[node]:
                if not visited[next_node]:
                    dist[next_node] = min(dist[next_node], dist[node] + graph[node][next_node])
                    queue.put((dist[next_node], next_node))
        visited[node] = True
        if visited[N]:
            break


for tc in range(1, T + 1):
    N, E = map(int, input().split())

    graph = {}
    for _ in range(E):
        s, e, w = map(int, input().split())
        if not graph.get(s):
            graph[s] = {}
        graph[s][e] = w

    visited = [0] * (N + 1)
    dist = [1e8] * (N + 1)
    dist[0] = 0
    dijkstra(0)
    print("#{} {}".format(tc, dist[N]))
