def fkwadratowa(a,b,c):
    delta = (b**2 - (4*a*c))
    x1 = ((-b-(delta ** 0.5))/(2*a))
    x2 = ((-b+(delta ** 0.5))/(2*a))
    x = ((-b )/ (2*a))
    if delta > 0:
         return x1, x2
    if delta == 0:
         return x
    if delta < 0:
         return None  
print(fkwadratowa(2,5,3))
