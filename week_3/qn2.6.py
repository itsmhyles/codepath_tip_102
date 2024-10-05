def identify_segments(terrain):
    segments = []
    count = 1
    n = len(terrain)
    
    for i in range(1, n):
        if terrain[i] == terrain[i - 1]:
            count += 1
        else:
            segments.append((terrain[i - 1], count))
            count = 1
    segments.append((terrain[-1], count))
    return segments

def count_balanced_terrain_subsections(terrain):
    segments = identify_segments(terrain)
    balanced_count = 0
    
    for i in range(len(segments) - 1):
        if segments[i][0] != segments[i + 1][0]:
            min_count = min(segments[i][1], segments[i + 1][1])
            balanced_count += min_count
    
    return balanced_count

# Test cases
print(count_balanced_terrain_subsections("00110011"))  # Should output 6
print(count_balanced_terrain_subsections("10101"))     # Should output 4