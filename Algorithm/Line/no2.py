def perm_r(k):
    global order
    global flag
    if k == R:
        order += 1
        if order == m:
            flag = True
    else:
        for i in range(N):
            if visited[i]:
                continue
            visited[i] = True
            c[k] = nums[i]
            perm_r(k + 1)
            if flag:
                return c
            visited[i] = False


nums = list(map(int, input().strip().split(' ')))
m = int(input())
nums = sorted(nums)
N = len(nums)
R = N
visited = [0] * N
c = [0] * R
order = 0
flag = False
print(''.join(list(map(str, perm_r(0)))))
