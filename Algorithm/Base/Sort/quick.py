import random
import time

"""
https://www.daleseo.com/sort-quick/
"""

random_lst = random.sample(range(100000), 100000)

start = time.time()


def quick_sort(lst, l, r):
    if r <= l:
        return

    def partition(low, high):
        pivot = lst[(low + high) // 2]

        while low <= high:
            while lst[low] < pivot:
                low += 1
            while lst[high] > pivot:
                high -= 1
            if low <= high:
                lst[low], lst[high] = lst[high], lst[low]
                low += 1
                high -= 1
        return low, high

    right_start, left_end = partition(l, r)
    quick_sort(lst, l, left_end)
    quick_sort(lst, right_start, r)

    return lst


quick_sort(random_lst, 0, len(random_lst) - 1)
# sorted(random_lst)
print(time.time() - start)
