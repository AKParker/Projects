import math

def isPalindrome(num):
    numList = list(str(num))
    
    for i in range(math.ceil(len(numList)/2)):
        if numList[i] != numList[-1-i]:
            return False

    return True

def nineHundreds():
    # 9's and 1's
    first = 999
    second = 991
    for firstFactor in range(10):
        for secondFactor in range(10):
            if isPalindrome((first-firstFactor*10) * (second-secondFactor*10)):
                return (first-firstFactor*10) * (second-secondFactor*10)

    thirds = 993
    for thirdFactor in range(10):
        for fourthFactor in range(10):
            if isPalindrome((thirds-thirdFactor*10) * (thirds-fourthFactor*10)):
                return (thirds-thirdFactor*10) * (thirds-fourthFactor*10)
