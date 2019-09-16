import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for idx in range(1,T+1):
    str1 = input()
    str2 = input()

    str_dict = {}

    for c in str1:
        if not str_dict.get(c):
            str_dict[c] = 0

    for c in str2:
        for k in str_dict:
            if k == c:
                str_dict[k] += 1

    maxi = 0
    for v in str_dict.values():
        if maxi < v:
            maxi = v

    print('#{} {}'.format(idx, maxi))