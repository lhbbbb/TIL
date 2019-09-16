import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for idx in range(1, T + 1):
    string = input()

    stack = []

    for c in string:
        if not stack:
            stack.append(c)
        else:
            if stack[-1] != c:
                stack.append(c)
            else:
                stack.pop()

    print('#{} {}'.format(idx, len(stack)))