# 정렬 알고리즘

## 1. 버블 정렬

$O(n^2)$의 시간복잡도를 갖는다.

## 2. 퀵 정렬(Quick sort)

트리의 깊이가 $logn$이고 각 깊이마다 $n$번의 연산을 하기 때문에 평균적으로 $O(nlogn)$의 시간복잡도를 갖는다. 매번 피벗을 잘못 잡는 최악의 경우 트리의 깊이가 $n$이 되므로 $O(n^2)$의 시간복잡도를 갖는다.

### 순서

1. 피벗을 정한다. => 리스트의 원소 중 랜덤하게 아무런 값을 잡는다.
2. 피벗보다 작은 값은 왼쪽으로, 큰 값은 오른쪽에 위치시킨다.
3. 1~2의 과정을 반복한다.

```python
def quick(lst):
    if len(lst) <= 1:
        return lst
    
    pivot = lst[len(lst) // 2]
    l = []
    r = []
    pivots = []
    for ele in lst:
        if ele < pivot:
            l.append(ele)
        elif ele == pivot:
            pivots.append(ele)
        else:
            r.append(ele)
    
    left = quick(l)
    right = quick(r)
    
    return left + pivots + right
```



## 3. 병합 정렬(Merge sort)

트리의 깊이가 $logn$이고 각 깊이마다 $n$번의 연산을 하기 때문에 $O(nlogn)$의 시간복잡도를 갖는다.

### 순서

1. 리스트의 원소가 1개 이하가 될때까지 이분할한다.
2. 분할된 리스트들의 첫번째 원소끼리 비교하며 작은 것부터 새로운 리스트의 첫번째 원소에 채워넣는다.
3. 분할된 리스트들이 빈 리스트가 될 때까지 2의 과정을 반복한다.

```python
def merge(lst):
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    l = merge(lst[:mid])
    r = merge(lst[mid:])
    
    sorted_lst = []
    while l or r:
        if l and r:
            if l[0] < r[0]:
                sorted_lst.append(l.pop(0))
            else:
                sorted_lst.append(r.pop(0))
        elif l:
            sorted_lst.append(l.pop(0))
        else:
            sorted_lst.append(r.pop(0))
  	
    return sorted_lst
```



## 4. Counting sort

$O(n)$의 시간복잡도를 갖는다. 하지만 리스트의 원소의 크기가 클수록 불필요한 메모리 공간을 낭비하고 무의미한 순회를 거쳐야 하기때문에 리스트의 최댓값이 작을 경우에만 쓰인다.

### 순서

1. 원소의 개수를 저장하는 배열 만들기
2. 누적합으로 정렬될 새로운 배열의 인덱스 구하기
3. 누적합 배열을 사용하여 정렬하기

```python
def counting(lst):
    c = [0] * (max(lst)+1)
	# 1.
    for ele in lst:
        c[ele] += 1
    
    # 2.
    for i in range(1, len(c)):
        c[i] = c[i-1]
        
    # 3.
    sorted_lst = [0] * len(lst)
    for ele in lst:
        sorted_lst[c[ele]-1] = ele
        c[ele] -= 1
```