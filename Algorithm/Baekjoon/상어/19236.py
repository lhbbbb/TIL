import sys

sys.stdin = open('input.txt', 'r')

board = [[0] * 4 for _ in range(4)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

res = 0


def find_low_num(n, lst):
    for i in range(4):
        for j in range(4):
            if lst[i][j][0] == -1 or lst[i][j][0] == 0:
                continue
            if lst[i][j][0] == n:
                return i, j

    return -1, -1


def check_move(x, y, lst):
    if 0 <= x < 4 and 0 <= y < 4:
        if lst[x][y][0] == -1:
            return False
        return True
    else:
        return False


def find_shark(lst):
    for i in range(4):
        for j in range(4):
            if lst[i][j][0] == -1:
                return i, j


def search(lst, score, k):
    global res

    ## 물고기 이동
    for n in range(1, 17):
        x, y = find_low_num(n, lst)
        if x == -1 and y == -1:
            continue
        ### 이동 가능한지 체크
        arrow = lst[x][y][1] - 1
        xx, yy = x + dx[arrow], y + dy[arrow]
        if check_move(xx, yy, lst):
            if lst[xx][yy][0] == 0:
                lst[xx][yy] = lst[x][y]
                lst[x][y] = (0, 0)
            else:
                lst[xx][yy], lst[x][y] = lst[x][y], lst[xx][yy]
        else:
            f = False
            for _ in range(7):
                arrow = (arrow + 1) % 8

                xx, yy = x + dx[arrow], y + dy[arrow]
                if check_move(xx, yy, lst):
                    lst[x][y] = (lst[x][y][0], arrow + 1)
                    if lst[xx][yy][0] == 0:
                        lst[xx][yy] = lst[x][y]
                        lst[x][y] = (0, 0)
                    else:
                        lst[xx][yy], lst[x][y] = lst[x][y], lst[xx][yy]
                    f = True
                if f:
                    break

        # for row in lst:
        #     print(row)
        # print()
    # 상어 이동
    s_x, s_y = find_shark(lst)
    s_arrow = lst[s_x][s_y][1] - 1
    s_xx, s_yy = s_x, s_y
    for _ in range(3):
        s_xx, s_yy = s_xx + dx[s_arrow], s_yy + dy[s_arrow]
        if 0 <= s_xx < 4 and 0 <= s_yy < 4:
            # 상어가 더이상 이동할 수 없으면 종료
            if lst[s_xx][s_yy][0] == 0:
                if score > res:
                    res = score
                continue

            new_score = score + lst[s_xx][s_yy][0]
            new_lst = [ele[:] for ele in lst]
            new_lst[s_xx][s_yy] = (-1, new_lst[s_xx][s_yy][1])
            new_lst[s_x][s_y] = (0, 0)

            search(new_lst, new_score, k + 1)

        # 상어가 더이상 이동할 수 없으면 종료
        else:
            if score > res:
                res = score
            continue


for i in range(4):
    info = list(map(int, input().split()))
    for j in range(4):
        board[i][j] = (info[j * 2], info[j * 2 + 1])

# init
## 상어 -1로 표현
init_score = board[0][0][0]
board[0][0] = (-1, board[0][0][1])
search(board, init_score, 0)
print(res)
