def terrain_elevation_match(terrain):
    
    '''
    Hint: Try using two variables: one to track the smallest available number and one for the largest. As you process each character in the string, 
    assign the smallest number when the next elevation should increase ('I'), and assign the largest number when the next elevation should decrease ('D').
    '''
    left = 0
    right = len(terrain)
    terrains = []
    
    for i in range(len(terrain)):
        if i == len(terrain)-1:
            if terrain[i] == "I":
                terrains.append(left)
                left +=1
            elif terrain[i] == "D":
                terrains.append(right)
                right -=1
        

        if terrain[i] == "I":
            terrains.append(left)
            left +=1
        
        elif terrain[i] == "D":
            terrains.append(right)
            right -=1
    
    return terrains

print(terrain_elevation_match("IDID")) 
print(terrain_elevation_match("III")) 
print(terrain_elevation_match("DDI")) 