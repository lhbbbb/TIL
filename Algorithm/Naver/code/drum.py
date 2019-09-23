def solution(drum):
    answer = 0
    aster_cnt = 0
    dy = [1, 0, 0]
    dx = [0, 1, -1]

    init_y, init_x = 0, 0
    y, x = 0, 0
    while init_x < len(drum):
        if drum[y][x] == "#":
            y += dy[0]
            x += dx[0]
        elif drum[y][x] == ">":
            y += dy[1]
            x += dx[1]
        elif drum[y][x] == "<":
            y += dy[2]
            x += dx[2]
        elif drum[y][x] == "*" and aster_cnt < 2:
            y += dy[0]
            x += dx[0]
            aster_cnt += 1

        if aster_cnt >= 2:
            init_y = 0
            init_x += 1
            y, x = init_y, init_x
            aster_cnt = 0
            continue
        if y == len(drum):
            answer += 1
            init_y = 0
            init_x += 1
            y, x = init_y, init_x

    return answer
