def count_endangered_species(endangered_species, observed_species):
    count = 0
    for i in range(len(observed_species)):
        if observed_species[i] in endangered_species:
            count += 1
    return count
   


''' Note to Self: 
    Need to learn how to use sets'''

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))  