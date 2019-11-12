# 퀵 정렬

> [출처](https://www.daleseo.com/sort-quick/)

## 기본 아이디어

* 병합 정렬과 마찬가지로 분할 정복기법과 재귀 알고리즘을 이용한 정렬 알고리즘

피봇(pivot)이라고 불리는 임의의 기준값을 사용합니다.

피봇값을 선택하는데는 여러가지 기준이 있지만 여기서는 편의상 중앙에 위치한 값을 사용하기로 합니다.

중앙에 피봇 값보다 작은 값을 왼편으로 몰고, 큰 값들은 모두 오른편으로 몰면 기준 값은 정렬된 위치에 놓이게 됩니다. 이 위치를 고정시키고 왼편과 오른편에 있는 값들을 같은 방식으로 반복해주면 피봇 값이 고정되면서 정렬이 완성됩니다.

## 시간복잡도

* pivot 값을 어떻게 설정하느냐에 따라 크게 달라질 수 있음
* 이상적인 경우에는 $O(nlogn)$의 시간복잡도를 가짐
* pivot값을 기준으로 분할했을 때 값들이 한 쪽으로 치우치는 최악의 경우에는 $O(n^2)$의 시간복잡도를 가짐

## 구현

* 리스트를 under-pivot, equal-pivot, upper-pivot의 3개로 구성하여 코드를 작성하면 직관적으론 이해하기 쉽지만 매번 새로운 리스트를 생성하기 때문에 메모리 사용 측면에서 비효율적
* 메모리 사용 측면에서 효율성을 가져오기 위해 in-place 정렬을 사용
* 기존 아이디어와 동일하게 값의 대소 비교를 위해  pivot값을 사용하지만, 분할의 기준점은 pivot 값이 아닐 수도 있음
  * ex) `[1,3,4,5,9,11,2,3,6]`
* 하지만 인덱스를 바꾸고 값을 교대하는 과정을 생각해보면, 결국 작은 것은 왼쪽에 큰 것은 오른쪽이라는 큰 틀은 바뀌지 않는다

```python
import random

random_lst = random.sample(range(100000), 100000)


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
```



