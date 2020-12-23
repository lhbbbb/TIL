import heapq


def solution(jobs):
    answer = 0
    N = len(jobs)
    # 1. 시작 요청이 가장 빠른 jobs 찾기
    jobs = sorted(jobs)
    init_job = jobs.pop(0)
    end_t = init_job[0] + init_job[1]
    answer += init_job[1]
    # 2. 대기 큐
    while jobs:
        tmp = []
        i = 0
        while i < len(jobs):
            if jobs[i][0] < end_t:
                job = jobs.pop(i)
                heapq.heappush(tmp, [job[1], job[0]])
                continue
            i += 1

        while tmp:
            cur_job = heapq.heappop(tmp)
            answer += (end_t - cur_job[1]) + cur_job[0]
            end_t += cur_job[0]

            j = 0
            while j < len(jobs):
                if jobs[j][0] < end_t:
                    job = jobs.pop(j)
                    heapq.heappush(tmp, [job[1], job[0]])
                    continue
                j += 1

        if jobs:
            nxt_job = jobs.pop(0)
            end_t += nxt_job[1]
            answer += nxt_job[1]

    answer //= N
    return answer
