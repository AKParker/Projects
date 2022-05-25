def sumOfSquares(num):
    # Takes a number and does the sum of squares from 1 to the number
    sum = 0
    for n in range(num):
        sum+=(n+1)**2

    return sum
