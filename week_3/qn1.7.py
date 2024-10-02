def post_compare(draft1, draft2):
    def process_draft(draft):
        # Initialize an empty stack
        stack = []
        
        # For each character c in draft:
        for c in draft:
            # If c is '#':
            if c == '#':
                # If stack is not empty:
                if stack:
                    # Pop from stack
                    stack.pop()
            else:
                # Push c onto stack
                stack.append(c)
        
        # Return stack as a string
        return ''.join(stack)

    # Compare processed drafts
    return process_draft(draft1) == process_draft(draft2)

print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b")) 