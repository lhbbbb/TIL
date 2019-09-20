N = int(input())

papers = []

for _ in range(N):
    a, b = map(int, input().split())

    if a < b:
        a, b = b, a
    papers.append((a, b))

papers.sort(reverse=True)
widths = [0] * 1000

for ele in papers:
    widths[ele[1]] = max(widths[ele[1]:]) + 1

print(max(widths))


###################
## solution2
# N = int(input())
#
# papers = []
#
# for _ in range(N):
#     a, b = map(int, input().split())
#
#     if a < b:
#         a, b = b, a
#     papers.append((a, b))
#
# papers.sort(reverse=True)
# candidates = papers
# cnt = 0
# while True:
#     tmp_cand = set()
#     for i in range(len(candidates)-1):
#         for j in range(i + 1, len(candidates)):
#            if candidates[i][1] >= candidates[j][1]:
#                 tmp_cand.add(candidates[j])
#     candidates = sorted(list(tmp_cand), reverse=True)
#     cnt += 1
#     # print(candidates)
#     if not tmp_cand:
#         break
#
# print(cnt)