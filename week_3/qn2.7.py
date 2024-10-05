def is_prefix_of_signal(transmission, searchSignal):
    # Split the transmission into individual signals
    signals = transmission.split()
    
    # Iterate through the signals
    for i, signal in enumerate(signals):
        # Check if the current signal starts with the searchSignal
        if signal.startswith(searchSignal):
            # Return the 1-indexed position of the signal
            return i + 1
    
    # If no match is found, return -1
    return -1

# Test cases
print(is_prefix_of_signal("i love eating burger", "burg"))  # Should output 4
print(is_prefix_of_signal("this problem is an easy problem", "pro"))  # Should output 2
print(is_prefix_of_signal("i am tired", "you"))  # Should output -1