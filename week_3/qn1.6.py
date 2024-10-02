def edit_post(post):
    # Split post into words
    words = post.split()
    
    # Initialize result list
    result = []
    
    # For each word in words:
    for word in words:
        # Initialize a queue (using a list)
        queue = list(word)
        
        # Initialize reversed_word as empty string
        reversed_word = ''
        
        # While queue is not empty:
        while queue:
            # Pop characters not dequeue
            char = queue.pop()
            # Add character to end of reversed_word
            reversed_word += char
            
        
        # Append reversed_word to result list
        result.append(reversed_word)

    # Join result list with spaces and return
    return ' '.join(result)

# Test the function
print(edit_post("Boost your engagement with these tips"))
print(edit_post("Check out my latest vlog"))