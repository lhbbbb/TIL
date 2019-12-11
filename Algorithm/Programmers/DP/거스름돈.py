'''
https://ydeer.tistory.com/59
'''
def solution(n, money):
    money_lst = [[0] * n for _ in range(len(money))]
    money.sort()
    for idx in range(money[0] - 1, n, money[0]):
        money_lst[0][idx] = 1
    for i in range(1, len(money)):
        for j in range(n):
            if j < i:
                money_lst[i][j] = money_lst[i - 1][j]
            elif j == money[i] - 1:
                money_lst[i][j] = money_lst[i - 1][j] + 1
            else:
                money_lst[i][j] = money_lst[i - 1][j] + money_lst[i][j - money[i]]

    answer = money_lst[-1][-1] % 1000000007
    return answer