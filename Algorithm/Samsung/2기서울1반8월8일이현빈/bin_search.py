import sys

sys.stdin = open('sample_input.txt', 'r')
# P  전체 쪽 수
# Pa  a가 찾아야할 쪽 번호
# Pb  b가 찾아야할 쪽 번호
T = int(input())
for idx in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())

    flag = True
    cnt_a, cnt_b = 0, 0
    a_l, b_l = 1, 1
    a_r, b_r = P, P
    while flag:
        a_center = int((a_l + a_r) / 2)
        b_center = int((b_l + b_r) / 2)

        if a_center == Pa:
            pass
        elif a_center < Pa:
            a_l = a_center
            cnt_a += 1
        else:
            a_r = a_center
            cnt_a += 1

        if b_center == Pb:
            pass
        elif b_center < Pb:
            b_l = b_center
            cnt_b += 1
        else:
            b_r = b_center
            cnt_b += 1

        if a_center == Pa and b_center == Pb:
            flag = False

    if cnt_a > cnt_b:
        print('#{} B'.format(idx))
    elif cnt_a < cnt_b:
        print('#{} A'.format(idx))
    else:
        print('#{} 0'.format(idx))
