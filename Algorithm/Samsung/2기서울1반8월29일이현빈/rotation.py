#import sys

#sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    lst = list(map(int, input().split()))

    for _ in range(M):
        front = lst.pop(0)
        lst.append(front)

    print('#{} {}'.format(tc, lst[0]))