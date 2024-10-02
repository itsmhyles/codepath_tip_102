def prioritize_observations(observed_species, priority_species):
    sorted_list = []

    for species in priority_species:
        sorted_list.extend([s for s in observed_species if s == species])
        sorted_list.extend([s for s in observed_species if s not in priority_species])

    return sorted_list

observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2)) 