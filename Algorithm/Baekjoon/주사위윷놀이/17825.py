lst = list(map(int, input().split()))

board = [0] * 501
board_dict = {}


def backtrack(k):
    global max_val
    if k == 10:
        player = [0] * 5
        player_loc = [0] * 5
        for i in range(10):
            loc = player_loc[visited[i]] + lst[i]
            if 0 <= loc <= 19 or 100 <= loc <= 103 or 200 <= loc <= 202 or 300 <= loc <= 303 or 400 <= loc <= 403:
                if loc == 5:
                    loc = 100
                elif loc == 10:
                    loc = 200
                elif loc == 15:
                    loc = 300
                if loc in player_loc:
                    return
                player_loc[visited[i]] = loc
            else:
                if loc == 20:
                    loc = 403
                elif 104 <= loc <= 107:
                    loc = 400 + (loc - 104)
                elif 203 <= loc <= 206:
                    loc = 400 + (loc - 203)
                elif 304 <= loc <= 307:
                    loc = 400 + (loc - 304)
                player_loc[visited[i]] = loc
                board_dict[player_loc[visited[i]]] = 0
            player[visited[i]] += board_dict[player_loc[visited[i]]]
        score = sum(player)
        if score > max_val:
            max_val = score
    else:
        for i in range(1, 5):
            visited[k] = i
            backtrack(k + 1)


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
backtrack(0)
print(max_val)
