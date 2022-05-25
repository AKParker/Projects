def sumEvenFibonacciNumbers():
    sumNum = 2
    fib1 = 1
    fib2 = 2
    fibNew = 3
    
    while fibNew < 4000000:
        fibNew = fib1 + fib2
        fib1 = fib2
        fib2 = fibNew

        if fibNew % 2 == 0:
            sumNum+=fibNew

    return sumNum
        
print(sumEvenFibonacciNumbers())
