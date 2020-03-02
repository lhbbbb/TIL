import sys
from collections import deque

sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def make_number(nums, side):
    for i in range(0, len(nums), side):
        num = ""
        for j in range(side):
            num += nums[i + j]
        res.add(num)


def str_to_num(s):
    return int(s, base=16)


for tc in range(1, T+1):
    N, K = map(int, input().split())
    numbers = deque(input())

    # 숫자 set
    res = set()

    # res가 K개 될때까지 반복
    nums_len = len(numbers)
    side = nums_len // 4
    ## init
    make_number(numbers, side)

    ## 반복
    for _ in range(1, side):
        numbers.rotate(1)
        make_number(numbers, side)

    ans = list(map(str_to_num, res))
    ans = sorted(ans, reverse=True)

    print('#{} {}'.format(tc, ans[K - 1]))
