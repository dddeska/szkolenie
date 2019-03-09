try:
    1/0
except ZeroDivisionError:
    print ("podzieliles przez 0")

lista = [1, 2, 3]
try:
    lista.funkcja()
except AttributeError:
    print("niezdefiniowana lista")

try: 
    lista[123]
except IndexError:
    print("bledna lista")

slownik = {
    "haslo" : "def"
}
try:
    slownik['nieistniejacy_klucz']
except KeyError:
    print("zly przyklad")

try: 
    while True:
        pass
except KeyboardInterrupt:
    print("koniec")

#wyjatki 

try:
    lista.funkcja()
except AttributeError:
    print("niezdefiniowana lista")


try:
    raise Exception("komunikat")
except Exception:
    print("komunikat")    
