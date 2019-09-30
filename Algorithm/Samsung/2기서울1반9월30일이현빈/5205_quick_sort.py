import sys

sys.stdin = open('sample_input.txt', 'r')


def partition(low, high, lst):
    pivot = lst[(low + high) // 2]
    while low <= high:
        # 좌측 찾기
        while lst[low] < pivot:
            low += 1
        # 우측 찾기
        while lst[high] > pivot:
            high -= 1
        if low <= high:
            lst[low], lst[high] = lst[high], lst[low]
            low += 1
            high -= 1
    return low


# Quick Sort
def quicksort(left, right, lst):
    if left >= right:
        return
    mid = partition(left, right, lst)
    quicksort(left, mid - 1, lst)
    quicksort(mid, right, lst)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split()))
    quicksort(0, len(a) - 1, a)

    print('#{} {}'.format(tc, a[len(a) // 2]))
