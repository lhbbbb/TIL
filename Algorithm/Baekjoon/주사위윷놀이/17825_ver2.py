dices = list(map(int, input().split()))

board = {0: [1, 2, 3, 4, 5], 1: [2, 3, 4, 5, 6], 2: [3, 4, 5, 6, 7], 3: [4, 5, 6, 7, 8], 4: [5, 6, 7, 8, 9],
         5: [22, 23, 24, 30, 31],
         6: [7, 8, 9, 10, 11], 7: [8, 9, 10, 11, 12], 8: [9, 10, 11, 12, 13], 9: [10, 11, 12, 13, 14],
         10: [25, 26, 30, 31, 32],
         11: [12, 13, 14, 15, 16], 12: [13, 14, 15, 16, 17], 13: [14, 15, 16, 17, 18], 14: [15, 16, 17, 18, 19],
         15: [27, 28, 29, 30, 31],
         16: [17, 18, 19, 20, 21], 17: [18, 19, 20, 21, 21], 18: [19, 20, 21, 21, 21], 19: [20, 21, 21, 21, 21],
         20: [21, 21, 21, 21, 21],
         21: [21, 21, 21, 21, 21], 22: [23, 24, 30, 31, 32], 23: [24, 30, 31, 32, 20], 24: [30, 31, 32, 20, 21],
         25: [26, 30, 31, 32, 20],
         26: [30, 31, 32, 20, 21], 27: [28, 29, 30, 31, 32], 28: [29, 30, 31, 32, 20], 29: [30, 31, 32, 20, 21],
         30: [31, 32, 20, 21, 21],
         31: [32, 20, 21, 21, 21], 32: [20, 21, 21, 21, 21]
         }

scores = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0, 13, 16, 19, 22, 24, 28, 27,
          26, 25, 30, 35]

horse_checker = [0 for _ in range(33)]


def backtrack(k, score, horse_loc):
    global max_val
    if k == 10:
        if max_val < score:
            max_val = score
    else:
        for i in range(4):
            next_loc = board[horse_loc[i]][dices[k] - 1]
            # goal in
            if horse_loc[i] == 21:
                continue

            if next_loc == 21:
                horse_checker[horse_loc[i]] = 0

                # update horse loc
                new_horse_loc = horse_loc[::]
                new_horse_loc[i] = next_loc
                backtrack(k + 1, score, new_horse_loc)
            else:
                if not horse_checker[next_loc]:
                    horse_checker[horse_loc[i]] = 0
                    new_score = score + scores[next_loc]
                    horse_checker[next_loc] = 1

                    # update horse loc
                    new_horse_loc = horse_loc[::]
                    new_horse_loc[i] = next_loc

                    backtrack(k + 1, new_score, new_horse_loc)
                    horse_checker[next_loc] = 0

            horse_checker[horse_loc[i]] = 1


horse = [0, 0, 0, 0]
max_val = 0

backtrack(0, 0, horse[::])

print(max_val)
