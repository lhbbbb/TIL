import re


def solution(word, pages):
    answer = 0
    w_p = re.compile('[a-z]+')
    cur_l_p = re.compile('<meta.*content=[\S]*')
    other_l_p = re.compile('<a href="https://[^"]*"')
    l_p = re.compile('"https://[^"]*"')

    basic = {}
    lnk = {}
    idx = 0
    for page in pages:
        tmp = page.lower()
        # 외부 링크 수
        cur_m = cur_l_p.search(tmp).group()
        cur_url = l_p.search(cur_m).group()
        if not basic.get(cur_url):
            basic[cur_url] = []
        m = other_l_p.findall(tmp)
        basic[cur_url].append(len(m))
        for ele in m:
            url = l_p.search(ele).group()
            if not lnk.get(url):
                lnk[url] = []
            lnk[url].append(cur_url)

        # 기본점수
        m = w_p.findall(tmp)
        basic[cur_url].append(m.count(word.lower()))
        basic[cur_url].append(idx)
        idx += 1

    max_val = 0
    for k in basic:
        lnk_score = 0
        # 링크 점수    
        if lnk.get(k):
            for ele in lnk[k]:
                lnk_score += (basic[ele][1] / basic[ele][0])
        # 매칭 점수
        match_score = basic[k][1] + lnk_score
        if match_score >= max_val:
            if match_score == max_val:
                if answer > basic[k][2]:
                    answer = basic[k][2]
            else:
                answer = basic[k][2]
            max_val = match_score

    return answer