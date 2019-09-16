import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for idx in range(1,T+1):
    N = int(input())
    info = []
    for i in range(N):
        info.append(list(map(int,input().split())))

    lst = [[0] * 10 for i in range(10)]
    cnt = 0
    for ele in info:
        for i in range(ele[0],ele[2]+1):
            for j in range(ele[1],ele[3]+1):
                if lst[i][j] != 0:
                    cnt +=1
                else:
                    lst[i][j] = ele[4]

    print('#{} {}'.format(idx, cnt))