import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def comb_r(k, s):
    if k == R:
        return cases.append((c[::], [x for x in people if x not in c]))
    else:
        for i in range(s, nums - R + 1 + k):
            c[k] = people[i]
            comb_r(k + 1, i + 1)


def find_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def find_cost(lst, depth):
    time_cnt = lst[0]
    lst = [x - lst[0] for x in lst]
    waiting = []
    queue = []
    while lst or queue or waiting:
        # 계단 도착
        while lst:
            if lst[0] == 0:
                waiting.append(lst.pop(0))
            else:
                break
        while waiting:
            if len(queue) < 3 and waiting[0] < 0:
                queue.append(0)
                waiting.pop(0)
            else:
                break
        for i in range(len(waiting)):
            waiting[i] -= 1

        # 계단 내려가기
        for i in range(len(queue)):
            queue[i] += 1
        if lst:
            for i in range(len(lst)):
                lst[i] -= 1
                if lst[i] < 0:
                    lst[i] = 0
        i = 0
        while i < len(queue):
            if queue[i] == depth:
                queue.pop(0)
            else:
                i += 1
        time_cnt += 1
    return time_cnt


for tc in range(1, T + 1):
    N = int(input())

    info = [list(map(int, input().split())) for _ in range(N)]

    people = []
    stairs = []
    for i in range(N):
        for j in range(N):
            if info[i][j] == 1:
                people.append((i, j))
            elif info[i][j] > 1:
                stairs.append((i, j))

    cases = []
    nums = len(people)
    for i in range(nums + 1):
        R = i
        c = [0] * R
        comb_r(0, 0)

    min_val = 1e9
    for case in cases:
        cost1, cost2 = 0, 0
        if case[0]:
            cost_lst = [find_dist(x, stairs[0]) for x in case[0]]
            cost1 = find_cost(sorted(cost_lst), info[stairs[0][0]][stairs[0][1]])
        if case[1]:
            cost_lst = [find_dist(x, stairs[1]) for x in case[1]]
            cost2 = find_cost(sorted(cost_lst), info[stairs[1][0]][stairs[1][1]])
        if cost1 < cost2:
            cost = cost2
        else:
            cost = cost1

        if min_val > cost:
            min_val = cost

    print('#{} {}'.format(tc, min_val))
