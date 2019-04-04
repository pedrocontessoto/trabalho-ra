
def Area(a,b,c):
    p = (a + b + c)/2
    A = (p * (p - a) * (p - b) * (p - c)) ** (1/2)
    return A

print(Area(2,6,8))