import sys

sys.stdin = open('input.txt', 'r')

N, M = map(int, input().strip().split(' '))
msgs = []
for _ in range(N):
    msgs.append(int(input()))

lst = [[0] * (100 * N) for _ in range(M)]

while msgs:
    time = msgs.pop(0)
    flag = False
    for i in range(100 * N):
        for j in range(M):
            if lst[j][i] == 0:
                lst[j][i:i + time] = [1] * time
                flag = True
                break
        if flag:
            break

all_val = []
for ele in lst:
    val = sum(ele)
    all_val.append(val)
print(max(all_val))
