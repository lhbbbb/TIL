lst = [4, 15, 6, 8, 10, 15]

max_val = max(lst)
c = [0] * (max_val + 1)
for ele in lst:
    c[ele] += 1

for i in range(1, len(c)):
    c[i] += c[i - 1]

res = [0] * len(lst)
for i in range(len(lst) - 1, -1, -1):
    res[c[lst[i]]-1] = lst[i]
    c[lst[i]] -= 1

print(res)