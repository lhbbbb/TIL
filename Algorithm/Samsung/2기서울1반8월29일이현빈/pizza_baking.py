#import sys

#sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    pizza_N = N
    queue = list(map(int, input().split()))
    pizza = []
    for i in range(1, N + 1):
        pizza.append((i, queue[i - 1]))

    i = 1
    flag = False
    while True:
        if i % pizza_N == 0:
            front = pizza.pop(0)
            pizza.append(front)
            pizza = [(x[0], x[1] // 2) for x in pizza]
        else:
            front = pizza.pop(0)
            pizza.append(front)
        if pizza[0][1] == 0:
            if N < M:
                pizza[0] = (N + 1, queue[N])
                N = N + 1
            else:
                pizza[0] = (0, 0)
                cnt = 0
                for ele in pizza:
                    if ele[0] == 0:
                        cnt += 1
                    if cnt == (pizza_N - 1):
                        flag = True
                        break
        if flag:
            break
        i += 1

    pizza_num = (0, 0)
    while pizza_num == (0, 0):
        pizza_num = pizza.pop()

    print('#{} {}'.format(tc, pizza_num[0]))
