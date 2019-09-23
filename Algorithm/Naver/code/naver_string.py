def solution(emails):
    name = "abcdefghijklmnopqrstuvwxyz."
    cnt = 0
    for ele in emails:
        if len(ele.split('@')) <= 1 or len(ele.split('.')) <= 1:
            continue
        if ele.count('@') >= 2:
            continue
        tmp = ele.split('@')
        # name
        flag_name = False
        for c in tmp[0]:
            if c not in name:
                flag_name = True
                break
        if flag_name:
            continue
        # domain
        domain_tmp = tmp[1].split('.')
        if not len(domain_tmp) == 2:
            continue
        if domain_tmp[0].isalpha() and domain_tmp[0].islower():
            pass
        else:
            continue
        # top level
        top_domain = ("com", "net", "org")
        if domain_tmp[1] not in top_domain:
            continue

        cnt += 1

    answer = cnt
    return answer


a = ["d@co@m.com", "a@abc.com", "b@def.com", "c@ghi.net"]
b = ["abc.def@x.com", "abc", "abc@defx", "abc@defx.xyz"]
print(solution(b))

