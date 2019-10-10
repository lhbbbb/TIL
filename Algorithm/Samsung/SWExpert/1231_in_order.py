import sys

sys.stdin = open('input.txt', 'r')

T = 10


def DFS(node):
    global string
    if not graph.get(node):
        visited[node] = True
        string += data[node]
    else:
        for next_node in graph[node]:
            DFS(next_node)
            if not visited[node]:
                visited[node] = True
                string += data[node]


for tc in range(1, T + 1):
    N = int(input())

    graph = {}
    data = {}
    for _ in range(N):
        lst = list(input().split())
        for i in range(len(lst)):
            if i != 1:
                lst[i] = int(lst[i])

        if len(lst) == 4:
            if not graph.get(lst[0]):
                graph[lst[0]] = []
            graph[lst[0]] += [lst[2]] + [lst[3]]
            if not data.get(lst[0]):
                data[lst[0]] = ""
            data[lst[0]] = lst[1]
        elif len(lst) == 3:
            if not graph.get(lst[0]):
                graph[lst[0]] = []
            graph[lst[0]] += [lst[2]]
            if not data.get(lst[0]):
                data[lst[0]] = ""
            data[lst[0]] = lst[1]
        else:
            if not data.get(lst[0]):
                data[lst[0]] = ""
            data[lst[0]] = lst[1]

    visited = [0] * (N + 1)
    string = ""
    DFS(1)
    print('#{} {}'.format(tc, string))
