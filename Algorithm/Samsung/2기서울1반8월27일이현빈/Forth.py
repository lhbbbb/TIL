#import sys

#sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for idx in range(1, T + 1):
    expression = input().split()

    operator = "*/+-"
    end = '.'
    stack = []
    res = 0
    for c in expression:
        if c not in operator and c != end:
            stack.append(c)
        elif c in operator:
            a = int(stack.pop())
            if not stack:
                print('#{} error'.format(idx))
                break
            b = int(stack.pop())
            if c == '+':
                res = b + a
                stack.append(res)
            elif c == '-':
                res = b - a
                stack.append(res)
            elif c == '*':
                res = b * a
                stack.append(res)
            else:
                res = b / a
                stack.append(res)
        elif c == end:
            res = stack.pop()
            if stack:
                print('#{} error'.format(idx))
            else:
                print('#{} {}'.format(idx, int(res)))
            break

