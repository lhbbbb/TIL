def solution(clothes):
    answer = 1

    types = {}
    # 1. init settings
    for name, t in clothes:
        if not types.get(t):
            types[t] = []
        
        types[t].append(name)

    # 2. find combination of cloth types
    for c_t in types:
        answer *= (len(types[c_t])+1)
    
    # 3. find all cases except wearing nothing
    answer -= 1

    return answer