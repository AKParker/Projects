def longestCollatzSequence(num):
    # Longest Collatz sequence under num
    longest = 1
    startNum = 1
    longestStart = 1
    while startNum < num:
        iterator = startNum
        currentChain = 1
        while iterator > 1:
            # If even
            if iterator%2==0:
                iterator/=2
                currentChain+=1
            # If odd
            else:
                iterator = 3*iterator + 1
                currentChain+=1
        if currentChain > longest:
            longest = currentChain
            longestStart = startNum
        startNum+=1

    return longestStart
