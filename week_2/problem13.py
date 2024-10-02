def navigate_research_station(station_layout, observations):
    total_distance = 0
    prev_index = None

    for ch in range(len(observations)):
        curr_index = station_layout.index(observations[ch])

        if prev_index is None:
            total_distance += curr_index
        
        if prev_index is not None:
            total_distance += abs(curr_index-prev_index)
        
        prev_index = curr_index
    
    return total_distance




station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))