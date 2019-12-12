import math


def solution(n, stations, w):
    answer = 0
    start = 0
    for station in stations:
        cnt = (station - w - 1 - start) / (2 * w + 1)
        cnt = math.ceil(cnt)
        answer += cnt
        start = station + w

    if n - start > 0:
        cnt = (n - start) / (2 * w + 1)
        cnt = math.ceil(cnt)
        answer += cnt

    return answer
