def silnia(n):
    wynik = 1
    for i in range(2, n+1):
        wynik = wynik * i 
    return(wynik)

print(silnia(5))
