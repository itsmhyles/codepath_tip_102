def count_explorers(explorers, supplies):
    # Convert lists to queues for easier manipulation
    explorer_queue = explorers.copy()
    supply_queue = supplies.copy()
    
    attempts = 0
    max_attempts = len(explorers) * len(supplies)  # Prevent infinite loop
    
    while explorer_queue and supply_queue and attempts < max_attempts:
        explorer = explorer_queue[0]
        supply = supply_queue[0]
        
        if explorer == supply:
            # Explorer gets the supply
            explorer_queue.pop(0)
            supply_queue.pop(0)
        else:
            # Explorer goes to the end of the queue
            explorer_queue.append(explorer_queue.pop(0))
        
        attempts += 1
    
    return len(explorer_queue)

# Test cases
print(count_explorers([1, 1, 0, 0], [0, 1, 0, 1]))  # Should output 0
print(count_explorers([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))  # Should output 3