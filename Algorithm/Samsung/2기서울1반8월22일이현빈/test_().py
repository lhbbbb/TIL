import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for idx in range(1, T + 1):
    code = input()

    stack = []
    check_lst = "{()}"
    check_back_lst = ")}"
    check_dict = {
        '(': ')',
        '{': '}',
    }
    flag = True
    for c in code:
        if c in check_lst:
            if c in check_back_lst:
                if not stack:
                    print('#{} {}'.format(idx, 0))
                    flag = False
                    break
                else:
                    k = stack.pop()
                    if check_dict[k] != c:
                        print('#{} {}'.format(idx, 0))
                        flag = False
                        break
            else:
                stack.append(c)

    if flag:
        if stack:
            print('#{} {}'.format(idx, 0))
        else:
            print('#{} {}'.format(idx, 1))
