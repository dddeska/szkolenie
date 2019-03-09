import csv

lata = []
wyniki = []

with open('przykladowy.csv', 'r') as f:
    czytacz = csv.DictReader(f)
    for wiersz in czytacz:
        rok = wiersz['Year']
        wynik = wiersz['Score']
        
        #1. przekonwertowanie na inty
        #2. dodawanie do listy

        lata.append(int(rok))
        wyniki.append(int(wynik))

############skrajne wyniki

min_wynik = wyniki[0]    
min_wynik_rok = lata[0]   
maks_wynik = wyniki[0] 
maks_wynik_rok = lata[0]

for rok, wynik in zip(lata, wyniki):

    if wynik < min_wynik:
        min_wynik = wynik
        min_wynik_rok = rok
    
    elif wynik > maks_wynik:
        maks_wynik = wynik
        maks_wynik_rok = rok

print("min", min_wynik, min_wynik_rok)
print("max", maks_wynik, maks_wynik_rok)

#srednia

srednia = sum(wyniki) / len(wyniki)
print(srednia)



