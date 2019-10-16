import sys
from collections import deque

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

oper = [1, -1, 2, -10]


def BFS(start, target):
    queue = deque([(start, 0)])
    visited[start] = True
    while queue:
        node, depth = queue.popleft()
        for i in range(4):
            if oper[i] == 1:
                res = node + 1
                if res == target:
                    return depth + 1
                if res <= 1000000:
                    if not visited[res]:
                        visited[res] = True
                        queue.append((res, depth + 1))
            elif oper[i] == -1:
                res = node - 1
                if res == target:
                    return depth + 1
                if res <= 1000000:
                    if not visited[res]:
                        visited[res] = True
                        queue.append((res, depth + 1))
            elif oper[i] == 2:
                res = node * 2
                if res == target:
                    return depth + 1
                if res <= 1000000:
                    if not visited[res]:
                        visited[res] = True
                        queue.append((res, depth + 1))
            else:
                res = node - 10
                if res == target:
                    return depth + 1
                if res <= 1000000:
                    if not visited[res]:
                        visited[res] = True
                        queue.append((res, depth + 1))


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    print('#{} {}'.format(tc, BFS(N, M)))

# todo: memory problem // how to optimize problem
