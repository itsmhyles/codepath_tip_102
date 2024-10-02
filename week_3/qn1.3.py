import re
def is_symmetrical_title(title):
    #remove all lowercase letters
    title = title.lower()
    #remove all non-alphanumeric characters
    title = re.sub(r'[^a-zA-Z0-9]', '', title)
    
    #create your two pointers
    left = 0
    right = len(title) -1

    #go through your two pointers
    while left < right:
        #if not palindrome, immediately return false
        if title[left] != title[right]:
            return False
        
        # go through the entire string
        left += 1
        right -= 1

    #default value
    return True


print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 
