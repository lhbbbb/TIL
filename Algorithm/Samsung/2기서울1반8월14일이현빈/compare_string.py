import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for idx in range(1, T + 1):
    pattern = input()
    text = input()

    # 보이어-무어 algorithm
    ## 1. 패턴 문자열의 끝이 일치하는지 확인
    N = len(pattern)
    M = len(text)

    index = 0
    cnt = 0
    while index < M:
        if pattern[N - 1] == text[index]:
            cnt = 0
            for i in range(N - 1, -1, -1):
                if pattern[i] == text[index - cnt]:
                    cnt += 1
                else:
                    index += cnt
                    break
        ## 2. 일치하지 않으면 패턴 문자열 중 text와 겹치는 문자가 있는지 확인
        else:
            shift = 0
            for i in range(N - 1, -1, -1):
                if pattern[i] == text[index]:
                    break
                else:
                    shift += 1
            index += shift

        if cnt == N:
            print("#{} 1".format(idx))
            break
    else:
        print("#{} 0".format(idx))
