lst = map(int, input().split())

board = [0] * 500
board_dict = {}
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