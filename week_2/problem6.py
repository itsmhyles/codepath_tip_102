def max_audience_performances(audiences):
    max_audience = max(audiences)
    audiences.pop(audiences.index(max_audience))
    for audience in audiences:
        if audience == max_audience:
            max_audience += audience
    return max_audience


audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))

''' def best_set(votes):
    freq = {}

    for vote, artist in votes.items():
        freq[artist] = freq.get(artist, 1) + 1 
    
    pair = []
    for artist, vote in freq.items():
        if len(pair) == 0:
            pair = [artist, vote]
        elif vote > pair[1]:
          print(artist, vote)
    return pair[0] '''
    
