import random
'''
https://www.daleseo.com/sort-quick/
'''
rand_lst = random.sample(range(20), 20)


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


quicksort(0, len(rand_lst) - 1, rand_lst)
print(rand_lst)
