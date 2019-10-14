N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]


def comb_r(k, s):
    if k == R:
        cases.append(c[::])
    else:
        for i in range(s, num - R + 1 + k):
            c[k] = chicken[i]
            comb_r(k + 1, i + 1)


def find_dist(points):
    city_dist = 0
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                candi = []
                for point in points:
                    candi.append(abs(i - point[0]) + abs(j - point[1]))
                dist = min(candi)
                city_dist += dist
    return city_dist


# 치킨집 개수, 좌표
chicken = []
num = 0
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append((i, j))
            num += 1
R = M
c = [0] * R

# 가능한 치킨집 좌표 조합
cases = []
comb_r(0, 0)

# 도시 치킨 거리
city_dist = 0
min_val = 1e8
for case in cases:
    city_dist = find_dist(case)
    if min_val > city_dist:
        min_val = city_dist

print(min_val)
