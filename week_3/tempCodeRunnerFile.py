
    if not logs:
        return concat_value
    else:
        while left<right:
            concat_value += int(str(logs[left]) + str(logs[right]))
            left +=1
            right -=1
        
        if left == right:
            concat_value += logs[left]
    
return concat_value