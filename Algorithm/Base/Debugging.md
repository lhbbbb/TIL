# Debugging

1. 문제 조건 정확히 다시 읽어볼 것
2. 테스트 케이스와 내 답의 출력형식이 정확히 일치하는지 확인
3. 내 전체적인 로직의 흐름이 맞는지 다시 한번 확인
4. 부분적인 로직들이 제대로 작동하는지 확인
5. 테스트 케이스 random으로 여러개 만들어서 확인

## Test Case 만들기

```python
import sys
# import random
# sys.stdout = open("input.txt", "w")
#
# print(1000)
# for T in range(1000):
#     N = random.randint(4, 100)
#     M = random.randint(1, N)
#     arr = [[0] * N for i in range(N)]
#
#     print(N, M)
#     for i in range(N):
#         for j in range(N):
#             t = random.randint(0, 2)
#             # if t == 2 and (i * j) % 10:
#             #     t = 0
#             # elif t == 1 and (i * j) % 5:
#             #     t = 0
#             print(t, end = ' ')
#         print()

import time

st = time.time()
sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(N)]
    a = 0
    for x in range(N):
        for y in range(M):
            a += b[x][y]
    print(a)
print(time.time() - st)
```



