def sredniaw(wartosci, wagi):
    licznik = 0
    mianownik = 0
    for wartosc, waga in zip(wartosci,wagi):
        licznik = wartosc * waga + licznik
        mianownik = waga + mianownik
    return (licznik/mianownik)

    



print (sredniaw([1, 2, 3],[1, 2, 3]))