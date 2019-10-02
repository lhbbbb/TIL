import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def BFS(i, j):
    queue = [(i, j, 0, info[i][j])]
    front, rear = -1, 0
    while front != rear:
        front += 1
        y, x, depth, numbers = queue[front]
        for k in range(4):
            next_y = y + dy[k]
            next_x = x + dx[k]
            if next_y >= 0 and next_y < 4 and next_x >= 0 and next_x < 4:
                if depth == 6:
                    cases.add(numbers)
                    continue
                queue.append((next_y, next_x, depth + 1, numbers + info[next_y][next_x]))
                rear += 1


for tc in range(1, T + 1):
    info = [input().split() for _ in range(4)]

    cases = set()
    for i in range(4):
        for j in range(4):
            BFS(i, j)
    print('#{} {}'.format(tc, len(cases)))
