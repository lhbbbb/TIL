def solution(enroll, referral, seller, amount):
    answer = []
    
    def calc_profit(k, money):
        if not graph.get(k):
            return
        else:
            tax = money // 10
            if tax >= 1:
                graph[k][1] += money - tax
                calc_profit(graph[k][0], tax)
            else:
                graph[k][1] += money
                return

    # 1. init settings
    graph = {}
    for i in range(len(enroll)):
        if not graph.get(enroll[i]):
            graph[enroll[i]] = []
        # [ref, profit]
        graph[enroll[i]].append(referral[i])
        graph[enroll[i]].append(0)

    # 2. calculate profit
    for i in range(len(seller)):
        calc_profit(seller[i], 100 * amount[i])
        
    
    for ele in enroll:
        answer.append(graph[ele][1])

    return answer