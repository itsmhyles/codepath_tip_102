def reverse_comments_queue(comments):
    #create stack
    list = []

    #iterate through the parameters
    for ele in comments:
        #add to stack
        list.append(ele)
    
    #replace values without returning a new data structure
    for i in range(len(list)):
       comments[i] = list.pop()
    
    
    return comments

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))
