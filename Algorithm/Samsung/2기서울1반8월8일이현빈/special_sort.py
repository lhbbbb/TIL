import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for idx in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))

    flag = True
    for i in range(len(A)):
        for j in range(i, len(A)):
            if flag:
                if A[i] < A[j]:
                    A[i], A[j] = A[j], A[i]
            else:
                if A[i] > A[j]:
                    A[i], A[j] = A[j], A[i]
        flag = not flag
    A = A[:10]
    print('#{} {}'.format(idx, ' '.join(list(map(str, A)))))
