from collections import Counter

def max_audience_performances(audiences):
    audience_counts = Counter(audiences)

    max_audience = max(audience_counts.keys())

    total_max_audience = max_audience * audience_counts[max_audience]
    return total_max_audience
    
audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))
