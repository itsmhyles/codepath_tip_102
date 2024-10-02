def identify_conflicts(venue1_schedule, venue2_schedule):
    common_values = venue1_schedule.items() & venue2_schedule.items()
    if common_values:
        return dict(common_values)


venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))

'''
def identify_conflicts(venue1_schedule, venue2_schedule):
    conflict = {}
    for (artist, time) in venue1_schedule.items():
        if artist in venue2_schedule and time == venue2_schedule[artist]:
          conflict[artist] = venue1_schedule[artist]
    return conflict
    '''
