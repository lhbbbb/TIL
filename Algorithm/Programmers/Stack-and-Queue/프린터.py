"""
my solution
"""
def solution(priorities, location):
    answer = 0
    while priorities:
        flag = False
        J = priorities[0]
        for ele in priorities:
            if J < ele:
                priorities.append(priorities.pop(0))
                location -= 1
                if location < 0:
                    location = len(priorities) - 1
                flag = True
                break
        else:
            priorities.pop(0)
            answer += 1
            if not flag and location == 0:
                break
            location -= 1
            if location < 0:
                location = len(priorities) - 1

    return answer

"""
solution2
인덱스 값과 인덱스에 해당하는 값을 동시에 어떻게 다를까 고민했었는데 enumerate를 사용하면 간단하게 해결..
"""
def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
