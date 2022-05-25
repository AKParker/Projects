import math

def isPrime(num):
    
    for n in range(math.ceil(num**.5)-1):
        if num%(n+2) == 0:
            return False
    return True

def sumOfPrimes(num):
    # Sum primes below num
    sumPrimes = 2 + 3 + 5
    for n in range(num-6):
        if isPrime(n+6):
            sumPrimes+=(n+6)

    return sumPrimes
