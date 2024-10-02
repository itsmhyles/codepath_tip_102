def most_endangered(species_list):
    new_list = []
    for i in range(len(species_list)):
        new_list.append(species_list[i]["population"])
    
    min_population = new_list.index(min(new_list))
    return species_list[min_population]["name"]



species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))