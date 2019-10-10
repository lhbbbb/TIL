import sys

sys.stdin = open('input.txt', 'r')

T = 10

for tc in range(1, 2):
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
    stack = [1]
    string = ""
    while stack:
        node = stack.pop()
        for next_node in reversed(graph[node]):
            if not visited[next_node]:
                stack.append(next_node)
            if not graph.get(next_node):
                visited[next_node] = True
                string += data[next_node]

    print('#{} {}'.format(tc, string))
