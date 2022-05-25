import math

def numFactors(num):
    # Prime numbers have two factors: 1 and themselves
    # Factors and divisors are used interchangably
    factors = 0
    for f in range(math.floor(num**.5)):
        if (f+1)**2 == num:
            factors+=1
            break
        if num%(f+1)==0:
            factors+=2

    return factors

def triangleNumbers():
    # Iterate through triangle numbers until one is found with > 500 factors
    triangleNum = 1
    iterator = 2
    while True:
        if numFactors(triangleNum) > 500:
            return triangleNum
        else:
            triangleNum+=iterator
            iterator+=1
