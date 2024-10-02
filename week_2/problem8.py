def num_popular_pairs(popularity_scores):
    count = {}
    for score in popularity_scores:
        if score in count:
            count[score] += 1
        else:
            count[score] = 1
    
    total_pairs = 0
    for score_count in count.values():
        if score_count > 1:
            pairs = (score_count * (score_count - 1)) // 2
            total_pairs += pairs
    
    return total_pairs

'''from collections import Counter

def num_popular_pairs(popularity_scores):
    
    #Count the occurences of each popularity score
    score_counts = Counter(popularity_scores)
    total_pairs = 0

    #For each unique score, calculate the number of pairs
    for count in score_counts.values():
        if count > 1:
            #Use the formula (n * (n-1)) / 2 to calculate pairs
            pairs = (count* (count - 1)) // 2
            total_pairs += pairs

    return total_pairs

'''

# Test cases
popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

print(num_popular_pairs(popularity_scores1))  # Output: 4
print(num_popular_pairs(popularity_scores2))  # Output: 6
print(num_popular_pairs(popularity_scores3))  # Output: 0
  

'''
Let's explain how this works:
We use Counter to count the occurrences of each popularity score.
For each unique score, we calculate the number of pairs it can form:
If a score appears n times, it can form (n * (n-1)) / 2 pairs.
This formula comes from the combination formula C(n,2).
We sum up all these pairs to get the total number of popular pairs.
Let's break down the examples:
For [1, 2, 3, 1, 1, 3]:
1 appears 3 times: (3 * 2) / 2 = 3 pairs
3 appears 2 times: (2 * 1) / 2 = 1 pair
Total: 3 + 1 = 4 pairs
For [1, 1, 1, 1]:
1 appears 4 times: (4 * 3) / 2 = 6 pairs
For [1, 2, 3]:
No number appears more than once, so 0 pairs
This solution is efficient as it only needs to iterate through the list once to count occurrences, and then once through the unique scores to calculate pairs. 
'''