def largestPrimeFactor(n):
    # every time you come across a factor, divide the number x by that factor
    divided = n
    
    while True:
        factor = 1
        
        while True:
            factor += 1
            if divided % factor == 0:
                divided /= factor
                break
            
        if divided == factor:
            print(factor, "factor")
            break

        print(divided, "divided")

largestPrimeFactor(600851475143)
