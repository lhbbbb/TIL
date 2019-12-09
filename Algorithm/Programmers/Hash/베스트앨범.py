def solution(genres, plays):
    genre_dic = {}
    for_sorted = {}
    answer = []
    for idx, genre in enumerate(genres):
        if not genre_dic.get(genre):
            genre_dic[genre] = {}
        genre_dic[genre][idx] = plays[idx]
        if not for_sorted.get(genre):
            for_sorted[genre] = 0
        for_sorted[genre] += plays[idx]

    s_genres = sorted(for_sorted, key=lambda x: for_sorted[x], reverse=True)

    for genre in s_genres:
        priority = sorted(genre_dic[genre], key=lambda x: genre_dic[genre][x], reverse=True)
        answer += priority[:2]

    return answer