import sys

sys.stdin = open('input1.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    info = [list(map(int, input().split())) for _ in range(N)]

    min_val = (100000, 0)
    for i in range(N):
        for j in range(N):
            tmp = []
            # 가로
            tmp += info[i]
            # 세로
            for k in range(N):
                if k != i:
                    tmp.append(info[k][j])

            unique = set(tmp)
            costs = []
            for ele in unique:
                cost = 0
                for item in tmp:
                    if ele == item:
                        continue
                    cost += abs(ele - item)
                costs.append((cost, ele))
            min_cost = sorted(costs)[0]
            if min_cost[0] < min_val[0]:
                min_val = min_cost
            elif min_cost[0] == min_val[0]:
                if min_val[1] > min_cost[1]:
                    min_val = min_cost

    print('#{} {} {}'.format(tc, min_val[0], min_val[1]))
