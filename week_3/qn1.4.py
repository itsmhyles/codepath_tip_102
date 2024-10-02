def engagement_boost(engagements):
    #Create Pointers
    left = 0
    right = len(engagements)-1

    '''Create a list with same length as parameter 
    initially filled with zeroes to
        1. pre-allocates memory for the entire result list upfront.
        2. and allow for direct index assignment (e.g., result[i] = ...).
        especially for two pointers

    '''
    result = [0] * len(engagements)

    '''
    Iterate through the loop from last index of parameter to
    0 and move backwards

    '''
    for i in range(len(engagements) -1, -1, -1):
        #compare absolute value of left and right:
        if abs(engagements[left])> abs(engagements[right]):
            result[i] = engagements[left] **2
            left +=1
        
        else:
            result[i] = engagements[right] * engagements[right]
            right -= 1

    return result

print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))