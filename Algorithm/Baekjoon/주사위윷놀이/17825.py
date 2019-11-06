lst = list(map(int, input().split()))

board = [0] * 501
board_dict = {}
for i in range(501):
    board_dict[i] = 0

def backtrack(k, score, tmp_loc, tmp):
    global max_val
    if k == 10:
        if score > max_val:
            max_val = score
    else:
        for i in range(1, 5):
            if k == 0:
                if i != 1:
                    continue
            visited[k] = i
            player = tmp[::]
            player_loc = tmp_loc[::]
            loc = player_loc[visited[k]] + lst[k]
            if 0 <= loc <= 19 or 100 <= loc <= 103 or 200 <= loc <= 202 or 300 <= loc <= 303 or 400 <= loc <= 403:
                if loc == 5:
                    loc = 100
                elif loc == 10:
                    loc = 200
                elif loc == 15:
                    loc = 300
            else:
                if loc == 20:
                    loc = 403
                elif 104 <= loc <= 107:
                    loc = 400 + (loc - 104)
                elif 203 <= loc <= 206:
                    loc = 400 + (loc - 203)
                elif 304 <= loc <= 307:
                    loc = 400 + (loc - 304)

            if loc in player_loc:
                continue
            player_loc[visited[k]] = loc
            player[visited[k]] += board_dict[player_loc[visited[k]]]
            backtrack(k + 1, sum(player), player_loc, player)


# normal route
for i in range(1, 20):
    board_dict[i] = i * 2

# 10 route
num = 13
board_dict[100] = 10
for i in range(101, 104):
    board_dict[i] = num
    num += 3

# 20 route
num = 22
board_dict[200] = 20
for i in range(201, 203):
    board_dict[i] = num
    num += 2

# 30 route
num = 28
board_dict[300] = 30
for i in range(301, 304):
    board_dict[i] = num
    num -= 1

# 25~40 route
num = 25
for i in range(400, 404):
    board_dict[i] = num
    num += 5

max_val = 0
visited = [0] * 10
cnt = 0
player = [0] * 5
player_loc = [0] * 5
backtrack(0, 0, player_loc, player)
print(max_val)
