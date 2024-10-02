def is_valid_post_format(posts):
    #create a stack
    top = []
    #iterate through the string
    for ch in posts:
        #identify if string is open parentheses
        if ch in "({[":
            #if open parentheses add to stack
            top.append(ch)
        else:
            # if stack is empty, never gna be a valid parenthesis
            if not top:
                return False
            
            #pop the last opening bracket from the stack
            match = top.pop()
            #check if the current closing bracket matches the popped opening bracket
            if ch == ")" and match != "(":
                return False
            if ch == "}" and match != "{":
                return False
            if ch == "]" and match != "[":
                return False

    #After processing all characters, the stack should be empty if all brackets were properly closed
    # Return True if the stack is empty, False otherwise
    return not top

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))

