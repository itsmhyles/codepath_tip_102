def first_symmetrical_landmark(landmarks):
  
    for landmark in landmarks:
        left = 0
        right = len(landmark)-1
        
        while left<right:
            if landmark[left] == landmark[right]:
                left +=1
                right -=1
            else:
                break

        if left>=right:
            return landmark

    return ""

print(first_symmetrical_landmark(["canyon","forest","rotor","mountain"])) 
print(first_symmetrical_landmark(["plateau","valley","cliff"]))