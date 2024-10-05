def find_the_log_conc_val(logs):
    concat_value = 0
    left = 0
    right=(len(logs)-1)
    
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

print(find_the_log_conc_val([7, 52, 2, 4])) 
print(find_the_log_conc_val([5, 14, 13, 8, 12])) 