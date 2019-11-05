# import sys

# sys.stdout = open('output.txt', 'w')

lst = list(map(int, input().split()))

board = [0] * 500
board_dict = {}


def backtrack(k, score, player_dict):
    global max_val
    if k == 10:
        if score > max_val:
            max_val = score
        # print(visited)
    else:
        for i in range(1, 5):
            if player[i]:
                continue
            new_player_dict = player_dict.copy()
            visited[k] = i
            new_player_dict[i] += lst[k]
            if 1 <= new_player_dict[i] <= 20 or 101 <= new_player_dict[i] <= 107 or 201 <= new_player_dict[
                i] <= 206 or 301 <= \
                    new_player_dict[i] <= 307:
                if not board[new_player_dict[i]]:
                    if new_player_dict[i] == 5:
                        new_player_dict[i] = 100
                    elif new_player_dict[i] == 10:
                        new_player_dict[i] = 200
                    elif new_player_dict[i] == 15:
                        new_player_dict[i] = 300
                    board[new_player_dict[i]] = True
                else:
                    player[i] = 0
                    board[new_player_dict[i]] = 0
                    return
            else:
                player[i] = True
                board_dict[new_player_dict[i]] = 0
            new_score = score + board_dict[new_player_dict[i]]
            backtrack(k + 1, new_score, new_player_dict)
            player[i] = 0


# normal route
for i in range(1, 21):
    board_dict[i] = i * 2

# 10 route
num = 13
board_dict[100] = 10
for i in range(101, 104):
    board_dict[i] = num
    num += 3

num = 25
for i in range(104, 108):
    board_dict[i] = num
    num += 5

# 20 route
num = 22
board_dict[200] = 20
for i in range(201, 203):
    board_dict[i] = num
    num += 2

num = 25
for i in range(203, 207):
    board_dict[i] = num
    num += 5

# 30 route
num = 28
board_dict[300] = 30
for i in range(301, 305):
    board_dict[i] = num
    num -= 1

num = 30
for i in range(305, 308):
    board_dict[i] = num
    num += 5

print(board_dict)
max_val = 0
visited = [0] * 10
player = [0] * 5
player_dict = {}
for i in range(1, 5):
    player_dict[i] = 0
backtrack(0, 0, [0, 0, 0, 0, 0])
print(max_val)
