import sys

sys.stdin = open("sample_input.txt", 'r')

T = int(input())


def merge_sort(lst):
    if len(lst) == 1:
        return lst

    middle = len(lst) // 2
    left = lst[:middle]
    right = lst[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(l, r):
    global cnt
    res = []
    if l[-1] > r[-1]:
        cnt += 1
    l_front = r_front = 0
    l_rear = len(l)
    r_rear = len(r)
    while l_front < l_rear or r_front < r_rear:
        if l_front < l_rear and r_front < r_rear:
            if l[l_front] <= r[r_front]:
                res.append(l[l_front])
                l_front += 1
            else:
                res.append(r[r_front])
                r_front += 1
        elif l_front < l_rear:
            res.append(l[l_front])
            l_front += 1
        elif r_front < r_rear:
            res.append(r[r_front])
            r_front += 1
    ## pop 사용 방법
    # while len(l) > 0 or len(r) > 0:
    #     if len(l) > 0 and len(r) > 0:
    #         if l[0] <= r[0]:
    #             res.append(l.pop(0))
    #         else:
    #             res.append(r.pop(0))
    #     elif len(l) > 0:
    #         res.append(l.pop(0))
    #     elif len(r) > 0:
    #         res.append(r.pop(0))

    return res


for tc in range(1, T + 1):
    N = int(input())

    a = list(map(int, input().split()))
    cnt = 0
    print('#{} {} {}'.format(tc, merge_sort(a)[N // 2], cnt))
