def clean_post(post):

    #dge cases
    if len(post) <2:
        return post
    

    else:
        #initialize an empty stack
        stack = []
        for ch in post:
            #Check if `c` is uppercase and matches the lowercase of the top stack item.
            if stack and ((ch.isupper() and stack[-1].lower() == ch.lower()) or 
            #Check if `c` is lowercase and matches the uppercase of the top stack item.
            (ch.islower() and stack[-1].upper() == ch.upper)):

                #If a matching pair is found, remove the top item from the stack.
                stack.pop()

            else:
                stack.append(ch)
    
    # Convert the remaining characters in the stack back to a string
    return ''.join(stack)

print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 

'''
Objective is to:
remove pairs of adhacent characters where one is lowercase and the other is an uppercase
There cannot be aA but there can be aa
an empty string is considered clean
'''