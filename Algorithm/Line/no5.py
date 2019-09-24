# 풀이 1
# def BFS(i, j):
#     queue = [(i, j, 0)]
#     front, rear = -1, 0
#     depth = 0
#     cnt = 0
#     time = 0
#     while front != rear:
#         front += 1
#         y, x, depth = queue[front]
#         for k in range(2):
#             next_y = y + dy[k]
#             next_x = x + dx[k]
#             if next_y <= M and next_x <= N:
#                 if board[next_y][next_x] == 1:
#                     queue.append((next_y, next_x, depth + 1))
#                     rear += 1
#                 elif board[next_y][next_x] == 2:
#                     cnt += 1
#                     time = depth + 1
#     return cnt, time


# N, M = map(int, input().split())
# run_x, run_y = map(int, input().split())
# dy = [1, 0]
# dx = [0, 1]
# if run_x > N or run_y > M:
#     print('fail')
# else:
#     board = [[0] * (N + 1) for _ in range(M + 1)]
#     for i in range(run_y + 1):
#         for j in range(run_x + 1):
#             board[i][j] = 1
#     board[run_y][run_x] = 2
#     cnt, time = BFS(0, 0)
#     print(time)
#     print(cnt)

# 풀이 2(순열)
N, M = map(int, input().split())
run_x, run_y = map(int, input().split())
if run_x > N or run_y > M:
    print('fail')
else:
    all_case = run_y + run_x
    fact = 1
    for i in range(1, all_case + 1):
        fact *= i

    fact_y = 1
    for i in range(1, run_y + 1):
        fact_y *= i

    fact_x = 1
    for i in range(1, run_x + 1):
        fact_x *= i

    print(all_case)
    print(fact // (fact_y * fact_x))
