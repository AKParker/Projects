def isPythagoreanTriplet(a,b,c):
    if a>=b or a>=c or b>=c:
        return False

    left = a**2 + b**2
    right = c**2
    if left == right:
        return True
    else:
        return False

def testing():
    # a has to be less than 333
    a=1
    while a < 333:
        # b has to be less than c but more than a
        b=a+1
        c=1000-a-b
        while b < c:
            if isPythagoreanTriplet(a,b,c):
                print("a: " + str(a) + "b: " + str(b) + "c: " + str(c))
                return a*b*c
            b+=1
            c-=1
        a+=1
