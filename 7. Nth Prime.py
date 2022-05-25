import math

def nthPrime(num):
    # num is the number n for nth primes you want to find
    # e.g. if num = 4, you want to find the 4th prime
    primeList = [2,3,5]
    currNum=6
    while len(primeList) < num:
        if isPrime(currNum):
            primeList.append(currNum)
        currNum+=1

    return primeList[-1]

def isPrime(num):
    
    for n in range(math.ceil(num**.5)-1):
        if num%(n+2) == 0:
            return False
    return True

