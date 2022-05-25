def threeOrFiveMultiplesSum(x):
    sumMultiples = 0
    for i in range(x):
        if i % 3 == 0 or i % 5 == 0:
            sumMultiples+=i

    return sumMultiples

