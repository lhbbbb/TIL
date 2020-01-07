def BFS(start, graph, n):
    queue = [(start, 0)]
    front, rear = -1, 0
    visited = [0] * (n + 1)
    visited[start] = True
    while front != rear:
        front += 1
        node, depth = queue[front]
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, depth + 1))
                rear += 1

    cnt = 0
    for node in queue:
        if node[1] == depth:
            cnt += 1

    return cnt


def solution(n, edge):
    answer = 0
    graph = {}
    for start, end in edge:
        if not graph.get(start):
            graph[start] = set()
        if not graph.get(end):
            graph[end] = set()

        graph[start].add(end)
        graph[end].add(start)

    answer = BFS(1, graph, n)
    return answer