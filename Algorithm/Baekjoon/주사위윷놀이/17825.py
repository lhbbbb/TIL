import sys

sys.stdout = open('output.txt', 'w')

lst = list(map(int, input().split()))

board = [0] * 500
board_dict = {}


def backtrack(k, point):
    global max_val
    if k == 10:
        score = 0
        for i in range(1, 5):
            if player_dict[i]:
                score += board_dict[player_dict[i]]

        if score > max_val:
            max_val = score
        print(visited)
    else:
        for i in range(1, 5):
            if player[i]:
                continue
            visited[k] = i
            player_dict[i] = point + lst[k]
            if 1 <= player_dict[i] <= 20 or 101 <= player_dict[i] <= 107 or 201 <= player_dict[i] <= 206 or 301 <= \
                    player_dict[i] <= 307:
                if player_dict[i] == 5:
                    player_dict[i] = 100
                elif player_dict[i] == 10:
                    player_dict[i] = 200
                elif player_dict[i] == 15:
                    player_dict[i] = 300
            else:
                player[i] = True
                board_dict[player_dict[i]] = 40
            backtrack(k + 1, player_dict[i])
            player[i] = 0


# normal route
for i in range(1, 21):
    board_dict[i] = i * 2

# 10 route
num = 13
for i in range(101, 104):
    board_dict[i] = num
    num += 3

num = 25
for i in range(104, 108):
    board_dict[i] = num
    num += 5

# 20 route
num = 22
for i in range(201, 203):
    board_dict[i] = num
    num += 2

num = 25
for i in range(203, 207):
    board_dict[i] = num
    num += 5

# 30 route
num = 28
for i in range(301, 305):
    board_dict[i] = num
    num -= 1

num = 30
for i in range(305, 308):
    board_dict[i] = num
    num += 5

max_val = 0
visited = [0] * 10
player = [0] * 5
player_dict = {}
for i in range(1, 5):
    player_dict[i] = 0
backtrack(0, 0)
print(max_val)
