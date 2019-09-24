N = int(input())

info = list(map(int, input().split()))

start, left_dist, right_dist, dist = 0, 0, 0, 0
max_dist = 0
for i in range(N):
    if info[i] == 0:
        left_dist = i - start
        for j in range(i + 1, N):
            if info[j] != 0:
                right_dist = j - i
                break
        if left_dist < right_dist:
            dist = left_dist
        else:
            dist = right_dist
        if max_dist < dist:
            max_dist = dist
    else:
        start = i

print(max_dist)
