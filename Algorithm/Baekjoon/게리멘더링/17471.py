N = int(input())

pop = list(map(int, input().split()))

graph = {}
for i in range(1, N + 1):
    info = list(map(int, input().split()))
    if not graph.get(i):
        graph[i] = set()
    graph[i].update(info[1:])


def comb_r(k, s):
    if k == R:
        case = [x for x in lst if x not in c]
        cases.append((c[::], case))
    else:
        for i in range(s, N - R + 1 + k):
            c[k] = lst[i]
            comb_r(k + 1, i + 1)


def BFS(start, info):
    queue = [start]
    front, rear = -1, 0
    visited[start] = True
    compare_set = {start}
    while front != rear:
        front += 1
        node = queue[front]
        for next_node in graph[node]:
            if not visited[next_node] and next_node in info:
                visited[next_node] = True
                queue.append(next_node)
                compare_set.add(next_node)
                rear += 1

    if set(info) == compare_set:
        return 1
    else:
        return 0


def BFS2(start):
    queue = [start]
    front, rear = -1, 0
    visited[start] = True
    while front != rear:
        front += 1
        node = queue[front]
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                rear += 1


visited = [0] * (N + 1)
cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        BFS2(i)
        cnt += 1
    if cnt >= 3:
        break

if cnt >= 3:
    print(-1)
else:
    lst = [x for x in range(1, N + 1)]
    cases = []
    for i in range(1, N // 2 + 1):
        R = i
        c = [0] * R
        comb_r(0, 0)
    # print(cases)
    min_val = 1e8
    for ele in cases:
        visited = [0] * (N + 1)
        total1 = 0
        if BFS(ele[0][0], ele[0]):
            for item in ele[0]:
                total1 += pop[item - 1]
        else:
            continue
        visited = [0] * (N + 1)
        total2 = 0
        if BFS(ele[1][0], ele[1]):
            for item in ele[1]:
                total2 += pop[item - 1]
        else:
            continue

        diff = abs(total1 - total2)
        if min_val > diff:
            min_val = diff

    print(min_val)
