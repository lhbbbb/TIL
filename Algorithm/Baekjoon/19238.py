import sys

sys.stdin = open('input.txt', 'r')

N, M, fuel = map(int, input().split())

start_board = [[0] * N for _ in range(N)]
end_board = [[0] * N for _ in range(N)]

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

res = M


def select_pas(x, y):
    global fuel
    queue = [(x, y, 0, 0)]
    front, rear = -1, 0
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    pas = []
    min_dis = 1000000
    if start_board[x][y]:
        pas.append((x, y, start_board[x][y]))
        return pas, 0

    while front != rear:
        front += 1
        loc_x, loc_y, flag, dis = queue[front]
        if flag:
            return pas, dis

        if fuel - dis < 0:
            return 0

        for k in range(4):
            xx, yy = loc_x + dx[k], loc_y + dy[k]
            if 0 <= xx < N and 0 <= yy < N and not visited[xx][yy] and start_board[xx][yy] != 1:
                visited[xx][yy] = 1
                if start_board[xx][yy] == 0:
                    queue.append((xx, yy, 0, dis + 1))
                else:
                    queue.append((xx, yy, 1, dis + 1))
                    if dis + 1 <= min_dis:
                        min_dis = dis + 1
                        pas.append((xx, yy, start_board[xx][yy]))
                rear += 1

    return 0


def move_des(x, y, target):
    global fuel
    queue = [(x, y, 0)]
    front, rear = -1, 0
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1

    if end_board[x][y] == target:
        return x, y, 0

    while front != rear:
        front += 1
        loc_x, loc_y, dis = queue[front]

        if fuel - dis < 0:
            return 0

        for k in range(4):
            xx, yy = loc_x + dx[k], loc_y + dy[k]
            if 0 <= xx < N and 0 <= yy < N and not visited[xx][yy] and end_board[xx][yy] != 1:
                visited[xx][yy] = 1
                if end_board[xx][yy] == 0:
                    queue.append((xx, yy, dis + 1))
                else:
                    if target in end_board[xx][yy]:
                        if (fuel - dis - 1) < 0:
                            return 0
                        end_board[xx][yy].remove(target)
                        if not end_board[xx][yy]:
                            end_board[xx][yy] = 0
                        return xx, yy, dis + 1
                    else:
                        queue.append((xx, yy, dis + 1))

                rear += 1

    return 0


for i in range(N):
    lst = list(map(int, input().split()))
    start_board[i] = lst[::]
    end_board[i] = lst[::]

tax_x, tax_y = map(int, input().split())
tax_x, tax_y = tax_x - 1, tax_y - 1

for i in range(2, M + 2):
    x, y, xx, yy = map(int, input().split())

    start_board[x - 1][y - 1] = i
    if end_board[xx - 1][yy - 1] == 0:
        end_board[xx - 1][yy - 1] = []
    end_board[xx - 1][yy - 1].append(i)

while True:
    # 1. 승객 선택
    tmp = select_pas(tax_x, tax_y)
    if tmp:
        pas, dis = tmp
        fuel -= dis
    else:
        print(-1)
        break
    ## 승객 우선순위
    pas = sorted(pas)
    start_board[pas[0][0]][pas[0][1]] = 0

    # 2. 목적지 이동
    tmp = move_des(pas[0][0], pas[0][1], pas[0][2])

    if tmp:
        tax_x, tax_y, dis = tmp
        res -= 1
        fuel -= dis
        fuel += dis * 2
    else:
        print(-1)
        break

    if res == 0:
        print(fuel)
        break
